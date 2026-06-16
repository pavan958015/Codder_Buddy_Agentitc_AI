from pydantic import BaseModel, Field, ConfigDict

class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path to the file to be modified")
    task_description: str = Field(
        description="A detailed description of the task to be performed on the file, e.g. 'add user authentication', 'implement data processing logic', etc."
    )

class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(
        description="A list of steps to be taken to implement the task"
    )
    model_config = ConfigDict(extra="allow")
