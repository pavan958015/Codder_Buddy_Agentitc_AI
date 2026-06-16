from pydantic import BaseModel, Field

class FileFeedback(BaseModel):
    filepath: str = Field(
        description="The relative path of the file that has issues"
    )
    comment: str = Field(
        description="Detailed comment describing the issue and how to fix it"
    )

class ReviewResult(BaseModel):
    approved: bool = Field(
        description="Whether the project code is approved and free of major bugs/syntax errors"
    )
    feedbacks: list[FileFeedback] = Field(
        description="List of feedbacks for specific files if not approved"
    )
