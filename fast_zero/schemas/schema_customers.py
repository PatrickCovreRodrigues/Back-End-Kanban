from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    id: int
    name: str
    description: str
    email: EmailStr
