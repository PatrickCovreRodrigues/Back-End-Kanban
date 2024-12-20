from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from http import HTTPStatus

from fast_zero.models.model import Todo, Activity
from fast_zero.schemas import TodoCreate, TodoRead 
from fast_zero.database import get_session

router = APIRouter()


@router.post('/', response_model=TodoRead, status_code=HTTPStatus.CREATED)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    activity = session.query(Activity).filter(Activity.id == todo.activity_id).first()
    if not activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Atividade não encontrada.'
        )
    new_todo = Todo(**todo.dict())
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)

    return new_todo


@router.get('/', response_model=List[TodoRead])
def read_tasks(session: Session = Depends(get_session)):
    todos = session.query(Todo).all()
    return todos


@router.get('/{todo_id}', response_model=TodoRead)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Tarefa não encontrada.'
        )

    return todo


@router.put('/{todo_id}', response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoCreate, session: Session = Depends(get_session)):
    db_todo = session.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Tarefa não encontrada.'
        )
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    

    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.delete('/{todo_id}', response_model=dict)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Tarefa não encontrada.'
        )
    session.delete(todo)
    session.commit()
    return {'detail': 'Tarefa deletada com sucesso!'}
