from datetime import datetime

from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    description: str
    email: EmailStr


class CustomerRead(BaseModel):
    id: int
    name: str
    description: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
