from datetime import datetime

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    id: int
    name: str
    description_project: str
    customer_id: int


class ProjectRead(BaseModel):
    project: list[ProjectCreate]
    created_at: datetime
