from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.models.database import get_session
from fast_zero.models.model import Activity, Todo, TodoState
from fast_zero.schemas.schemaTodo import TodoCreate, TodoList, TodoSchema
from fast_zero.utils.validUtils import is_valid_state_transition

router = APIRouter(prefix='/todos', tags=['todos'])


@router.get('/', response_model=TodoList)
def list_todos(
    session: Session = Depends(get_session),
    states: List[TodoState] | None = Query(None),
    exclude_trash: bool = True,
    title: str | None = None,
    description: str | None = None,
    offset: int = 0,
    limit: int = 10,
):
    query = select(Todo)

    if states:
        query = query.where(Todo.state.in_(states))

    if exclude_trash:
        query = query.where(Todo.state != TodoState.trash)

    if title:
        query = query.where(Todo.title.contains(title))

    if description:
        query = query.where(Todo.description_activity.contains(description))

    todos = session.scalars(query.offset(offset).limit(limit)).all()

    return {'todos': todos}


@router.post('/', response_model=dict)
def create_todo(
    todo: TodoCreate,
    session: Session = Depends(get_session),
):
    activity = session.query(Activity).where(Activity.id == todo.activity_id).first()

    if not activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Não existe essa atividade')

    new_todo = Todo(
        title=todo.title,
        description_activity=todo.description_activity,
        state=todo.state,
        activity_id=activity.id,
    )

    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)

    return {"message": "Atualização da atividade feita!", "id": new_todo.id}


@router.patch('/{todo_id}/state', response_model=TodoSchema)
def update_todo_state(
    todo_id: int,
    new_state: TodoState,
    session: Session = Depends(get_session),
):
    db_todo = session.scalar(select(Todo).where(Todo.id == todo_id))
    if not db_todo:
        raise HTTPException(
            status_code=404,
            detail='Tarefa não encontrada.'
        )

    if not is_valid_state_transition(db_todo.state, new_state):
        raise HTTPException(
            status_code=400,
            detail=f'Transição de estado de {db_todo.state} para {new_state} não é permitida.'
        )

    db_todo.state = new_state
    session.commit()
    session.refresh(db_todo)

    return db_todo


@router.delete('/{todo_id}', response_model=dict)
def delete_todo(
    todo_id: int,
    session: Session = Depends(get_session),
):
    db_todo = session.scalar(select(Todo).where(Todo.id == todo_id))
    if not db_todo:
        raise HTTPException(
            status_code=404,
            detail='Tarefa não encontrada.'
        )

    session.delete(db_todo)
    session.commit()

    return {'message': 'Success'}
