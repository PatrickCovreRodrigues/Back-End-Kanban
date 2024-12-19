from pydantic import BaseModel
from datetime import datetime


class ProjectCreate(BaseModel):
    id: int
    name: str
    description_project: str
    created_at: datetime
    customer_id: int
    
    class Config:
        orm_mode = True


class ProjectRead(BaseModel):
    project: list[ProjectCreate]
