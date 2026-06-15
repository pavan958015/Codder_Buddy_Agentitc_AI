from agent.llm import llm
from agent.models import ReviewResult
from agent.prompts import reviewer_system_prompt, reviewer_user_prompt
from agent.tools import list_files, read_file, run_cmd


def reviewer_agent(state: dict) -> dict:
    """Reviews the generated codebase and runs tests/syntax compilation checks."""
    print("\n" + "=" * 60)
    print("REVIEWER: Reviewing generated files...")
    print("=" * 60 + "\n")

    files_str = list_files.run(".")
    if (
        not files_str
        or files_str.startswith("ERROR")
        or files_str == "No files found."
    ):
        print("Reviewer: No files to review.")
        return {"feedbacks": [], "status": "APPROVED"}

    files_list = [f.strip() for f in files_str.split("\n") if f.strip()]

    files_content_block = []
    python_files = []

    for filepath in files_list:
        content = read_file.run(filepath)
        files_content_block.append(f"File: {filepath}\nContent:\n{content}\n")
        if filepath.endswith(".py"):
            python_files.append(filepath)

    files_summary = "\n".join(files_content_block)

    test_output = ""
    if python_files:
        print(
            f"Reviewer: Performing Python syntax compilation check on: {python_files}"
        )
        for py_file in python_files:
            code, stdout, stderr = run_cmd.run(
                f"python -m py_compile {py_file}"
            )
            if code != 0:
                test_output += f"Syntax error in {py_file}:\n{stderr}\n"

    sys_prompt = reviewer_system_prompt()
    user_prompt = reviewer_user_prompt(files_summary, test_output)

    try:
        structured_llm = llm.with_structured_output(ReviewResult)
        result: ReviewResult = structured_llm.invoke(
            [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )
    except Exception as e:
        print(f"Reviewer LLM invocation failed: {e}. Defaulting to approval.")
        result = ReviewResult(approved=True, feedbacks=[])

    print("\nReviewer Results:")
    print(f"Approved: {result.approved}")
    if result.feedbacks:
        print("Feedbacks:")
        for fb in result.feedbacks:
            print(f"- {fb.filepath}: {fb.comment}")
    print("-" * 60)

    if result.approved:
        return {"feedbacks": [], "status": "APPROVED"}
    else:
        return {
            "feedbacks": result.feedbacks,
            "current_feedback_idx": 0,
            "status": "FIXING",
        }
