from datetime import datetime

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description_project: str
    customer_id: int


class ProjectRead(BaseModel):
    id: int
    name: str
    description_project: str
    customer_id: int
    created_at: datetime

    class Config:
        orm_mode = True
