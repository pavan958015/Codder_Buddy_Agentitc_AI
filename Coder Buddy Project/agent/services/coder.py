from langgraph.prebuilt import create_react_agent
from agent.llm import llm
from agent.models import CoderState
from agent.prompts import coder_system_prompt
from agent.tools import read_file, write_file, list_files, get_current_directory, get_template


def coder_agent(state: dict) -> dict:
    """LangGraph tool-using coder agent."""

    feedbacks = state.get("feedbacks", [])
    coder_tools = [
        read_file,
        write_file,
        list_files,
        get_current_directory,
        get_template,
    ]

    if feedbacks:
        # Coder is in feedback-fixing loop
        current_feedback_idx = state.get("current_feedback_idx", 0)

        if current_feedback_idx >= len(feedbacks):
            print("\nAll feedback items addressed. Re-running reviewer...\n")
            return {
                "feedbacks": [],
                "current_feedback_idx": 0,
                "status": "DONE",
            }

        feedback = feedbacks[current_feedback_idx]
        print(
            f"\nAddressing feedback [{current_feedback_idx + 1}/{len(feedbacks)}] "
            f"for {feedback.filepath}"
        )

        existing_content = read_file.run(feedback.filepath)
        system_prompt = coder_system_prompt()
        user_prompt = (
            f"Task: Address code review feedback and fix the file.\n\n"
            f"File: {feedback.filepath}\n\n"
            f"Review Feedback: {feedback.comment}\n\n"
            f"Existing Content:\n{existing_content}\n\n"
            f"You MUST fix the issue, generate the complete file content, and "
            f"use write_file(path, content) to save it."
        )

        react_agent = create_react_agent(model=llm, tools=coder_tools)

        response = react_agent.invoke(
            {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ]
            }
        )

        print("\nCoder Response (Fix):")
        print(response)
        print("-" * 60)

        return {"current_feedback_idx": current_feedback_idx + 1}

    # Normal generation phase
    coder_state: CoderState = state.get("coder_state")

    if coder_state is None:
        coder_state = CoderState(
            task_plan=state["task_plan"], current_step_idx=0
        )

    steps = coder_state.task_plan.implementation_steps

    if coder_state.current_step_idx >= len(steps):
        print("\nAll files generated successfully.\n")
        return {"coder_state": coder_state, "status": "DONE"}

    current_task = steps[coder_state.current_step_idx]

    print(
        f"\nGenerating [{coder_state.current_step_idx + 1}/{len(steps)}] "
        f"{current_task.filepath}"
    )

    existing_content = read_file.run(current_task.filepath)

    system_prompt = coder_system_prompt()

    user_prompt = (
        f"Task: {current_task.task_description}\n\n"
        f"File: {current_task.filepath}\n\n"
        f"Existing Content:\n{existing_content}\n\n"
        f"You MUST generate the complete file content and "
        f"use write_file(path, content) to save it."
    )

    react_agent = create_react_agent(model=llm, tools=coder_tools)

    response = react_agent.invoke(
        {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        }
    )

    print("\nCoder Response:")
    print(response)
    print("-" * 60)

    coder_state.current_step_idx += 1

    return {"coder_state": coder_state}
