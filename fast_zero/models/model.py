from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Enum, ForeignKey, func
from sqlalchemy.orm import Mapped, relationship, mapped_column, registry

table_registry = registry()


class TodoState(str, PyEnum):
    PENDING = 'Pendente'
    TODO = 'A fazer'
    IN_PROGRESS = 'Em progresso'
    STAND_BY = 'Em espera'
    DONE = 'Feito'


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
    activities = relationship("Activity", back_populates="project", cascade="all, delete")


@table_registry.mapped_as_dataclass
class Activity:
    __tablename__ = 'activitys'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    description_activity: Mapped[str]
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'))
    status: Mapped[str] = mapped_column(Enum(TodoState), default=TodoState.PENDING)
    created_at: Mapped[datetime] = mapped_column(
         # pylint: disable=not-callable
        init=False, server_default=func.now()
    )

    project = relationship("Project", back_populates="activities")
