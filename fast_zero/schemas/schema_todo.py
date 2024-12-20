from typing import List, Optional

from pydantic import BaseModel

import enum

class TodoState(str, enum.Enum):
    PENDING = "Pendente"
    TODO = "A Fazer"
    IN_PROGRESS = "Fazendo"
    ON_HOLD = "Parado"
    DONE = "Concluído"


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState


class TodoList(BaseModel):
    todos: list[TodoSchema]


class TodoCreate(TodoSchema):
    pass


class TodoRead(TodoSchema):
    id: int
    activity_id: int

    class Config:
        orm_mode = True


class ActivityBase(BaseModel):
    name: str
    description_activity: str
    project_id: int


class ActivityCreate(ActivityBase):
    pass


class ActivityRead(ActivityBase):
    id: int
    todos: list[TodoRead] = []

    class Config:
        orm_mode = True
