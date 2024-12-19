from pydantic import BaseModel

from fast_zero.models.model import TodoState


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState


class TodoList(BaseModel):
    todos: list[TodoSchema]


class TodoCreate(BaseModel):
    title: str
    description_activity: str
    state: TodoState
    activity_id: int
