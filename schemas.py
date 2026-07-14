from pydantic import BaseModel
from typing import Literal


class TaskCreate(BaseModel):
    title: str
    description: str
    status: Literal["Pending", "Completed"] = "Pending"


class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True
