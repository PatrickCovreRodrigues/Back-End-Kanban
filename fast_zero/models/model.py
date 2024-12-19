from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


class TodoState(str, Enum):
    draft = 'draft'
    todo = 'todo'
    doing = 'doing'
    done = 'done'
    trash = 'trash'


VALID_STATE_TRANSITIONS = {
    TodoState.draft: [TodoState.todo],
    TodoState.todo: [TodoState.doing, TodoState.trash],
    TodoState.doing: [TodoState.done, TodoState.todo],
    TodoState.done: [TodoState.trash],
    TodoState.trash: [],
}


@table_registry.mapped_as_dataclass
class Todo:
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    description_activity: Mapped[str]
    state: Mapped[TodoState]

    activity_id: Mapped[int] = mapped_column(ForeignKey('activitys.id'))


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        # pylint: disable=not-callable
        init=False, server_default=func.now()
    )


@table_registry.mapped_as_dataclass
class Project:
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    description_project: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
         # pylint: disable=not-callable
        init=False, server_default=func.now()
    )

    customer_id: Mapped[int] = mapped_column(ForeignKey('users.id'))


@table_registry.mapped_as_dataclass
class Activity:
    __tablename__ = 'activitys'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    description_activity: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
         # pylint: disable=not-callable
        init=False, server_default=func.now()
    )

    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'))
