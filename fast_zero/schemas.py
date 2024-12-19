from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    description: str
    email: EmailStr


class Customer(CustomerCreate):
    id: int

    class Config:
        orm_mode = True
