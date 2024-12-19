from datetime import datetime

from pydantic import BaseModel


class ActivityCreate(BaseModel):
    id: int
    name: str
    description_activity: str
    project_id: int


class ActivityRead(BaseModel):
    activity: list[ActivityCreate]
    created_at: datetime
