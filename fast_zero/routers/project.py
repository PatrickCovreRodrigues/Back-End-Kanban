from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.models.database import get_session
from fast_zero.models.model import Project, User
from fast_zero.schemas.schema_message import Message
from fast_zero.schemas.schema_project import ProjectCreate, ProjectRead

router = APIRouter(
    prefix='/projects',
    tags=['projects'],
)


@router.post('/', status_code=HTTPStatus.CREATED, response_model=ProjectRead)
def project_created(project: ProjectCreate, session: Session = Depends(get_session)):
    customer_exists = session.scalar(
        select(User).where(User.id == project.customer_id)
    )
    if not customer_exists:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não existe!'
        )

    new_project = Project(
        name=project.name,
        description_project=project.description_project,
        customer_id=project.customer_id
    )
    session.add(new_project)
    session.commit()
    session.refresh(new_project)

    return new_project


@router.get('/', response_model=List[ProjectRead])
def read_all_project(session: Session = Depends(get_session)):
    project_db = session.scalars(select(Project)).all()
    if not project_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Não existe projetos!'
        )
    return project_db


@router.get('/{project_id}', response_model=ProjectCreate)
def read_id_project(project_id: int, session: Session = Depends(get_session)):
    project_db = session.scalar(select(Project).where(project_id == Project.id))
    if not project_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )
    return project_db


@router.get('/{project_id}/activities_with_tasks')
async def get_activities_with_tasks(project_id: int, session: Session = Depends(get_session)):
    project_db = session.scalar(select(Project).where(Project.id == project_id))
    if not project_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )
    return project_db


@router.put('/{project_id}', response_model=ProjectCreate)
def update_project(
    project_id: int,
    project: ProjectCreate,
    session: Session = Depends(get_session)
):
    project_db = session.scalar(select(Project).where(Project.id == project_id))
    if not project_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )
    customer_exists = session.scalar(select(User).where(User.id == project.customer_id))
    if not customer_exists:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado!'
        )
    project_db.name = project.name
    project_db.description_project = project.description_project
    project_db.customer_id = project.customer_id
    session.commit()
    session.refresh(project_db)

    return project_db


@router.delete('/{project_id}', response_model=Message)
def delete_project(project_id: int, session: Session = Depends(get_session)):
    project_db = session.scalar(select(Project).where(Project.id == project_id))
    if not project_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )
    session.delete(project_db)
    session.commit()
    return {'message': 'Projeto deletado!'}
