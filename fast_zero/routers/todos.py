# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from http import HTTPStatus

# from fast_zero.models.model import Todo, Activity
# from fast_zero.schemas import TodoCreate, TodoRead, TodoState
# from fast_zero.database import get_session

# router = APIRouter()


# @router.post('/', response_model=TodoRead, status_code=HTTPStatus.CREATED)
# def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
#     try:
#         print(f"Dados recebidos: {todo.dict()}")  # Log dos dados recebidos

#         # Verificar se a atividade existe
#         activity = session.query(Activity).filter(Activity.id == todo.activity_id).first()
#         if not activity:
#             raise HTTPException(
#                 status_code=HTTPStatus.NOT_FOUND,
#                 detail='Atividade não encontrada.'
#             )

#         # Criar o novo 
#         new_todo = Todo(
#             title='Pendente',
#             activity_id=4,
#             state=TodoState..value
#         )
#         session.add(new_todo)
#         session.commit()
#         session.refresh(new_todo)

#         return new_todo

#     except Exception as e:
#         print(f"Erro ao criar : {e}")  # Log do erro
#         raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=f"Erro ao criar : {e}")


# @router.get('/', response_model=List[TodoRead])
# def read_tasks(session: Session = Depends(get_session)):
#     todos = session.query(Todo).all()
#     return todos


# @router.get('/{todo_id}', response_model=TodoRead)
# def read_todo(todo_id: int, session: Session = Depends(get_session)):
#     todo = session.query(Todo).filter(Todo.id == todo_id).first()
#     if not todo:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND,
#             detail='Tarefa não encontrada.'
#         )

#     return todo


# @router.put('/{todo_id}', response_model=TodoRead)
# def update_todo_state(todo_id: int, todo: TodoCreate, session: Session = Depends(get_session)):
#     db_todo = session.query(Todo).filter(Todo.id == todo_id).first()
#     if not db_todo:
#         raise HTTPException(
#             status_code=404,
#             detail="Tarefa não encontrada."
#         )
#     db_todo.state = todo.state
#     session.commit()
#     session.refresh(db_todo)
#     return db_todo


# @router.delete('/{todo_id}', response_model=dict)
# def delete_todo(todo_id: int, session: Session = Depends(get_session)):
#     todo = session.query(Todo).filter(Todo.id == todo_id).first()
#     if not todo:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND,
#             detail='Tarefa não encontrada.'
#         )
#     session.delete(todo)
#     session.commit()
#     return {'detail': 'Tarefa deletada com sucesso!'}
