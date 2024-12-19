from datetime import datetime

from pydantic import BaseModel


class ActivityCreate(BaseModel):
    id: int
    name: str
    description_activity: str
    project_id: int


class ActivityRead(BaseModel):
    id: int
    name: str
    description_activity: str
    project_id: int
    created_at: datetime

    class Config:
        orm_mode = True
