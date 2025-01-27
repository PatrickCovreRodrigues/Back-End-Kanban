from datetime import datetime

from pydantic import BaseModel

from fast_zero.models.model import TodoState


class ActivityCreate(BaseModel):
    name: str
    description_activity: str
    status: TodoState
    project_id: int


class ActivityRead(BaseModel):
    id: int
    name: str
    description_activity: str
    project_id: int
    status: TodoState
    created_at: datetime

    class Config:
        orm_mode = True
