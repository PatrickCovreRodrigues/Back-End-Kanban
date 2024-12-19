from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.models.database import get_session

# from fast_zero.models.model import Activity, User
from fast_zero.models.model import Activity, Project
from fast_zero.schemas.schema_activity import ActivityCreate
from fast_zero.schemas.schemaMessage import Message

router = APIRouter(
    prefix='/activitys',
    tags=['activitys'],
)


@router.post('/', status_code=HTTPStatus.CREATED, response_model=ActivityCreate)
def activity_created(activity: ActivityCreate, session: Session = Depends(get_session)):
    project = session.scalar(
        select(Project).where(Project.id == activity.project_id)
    )
    if not project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não existe!'
        )
    activity_creat = session.scalar(
        select(Activity).where(Activity.id == activity.id)
    )
    if activity_creat:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Atividade já existe!'
        )
    new_activity = Activity(
        name=activity.name,
        description_activity=activity.description_activity,
        project_id=activity.project_id
    )
    session.add(new_activity)
    session.commit()
    session.refresh(new_activity)

    return new_activity


@router.get('/{activity_id}', response_model=ActivityCreate)
def read_activity(
    activity_id: int,
    session: Session = Depends(get_session)
):
    db_activity = session.scalar(select(Activity).where(Activity.id == activity_id))
    if not db_activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Atividade não encontrada!'
        )
    return db_activity


@router.put('/{activity_id}', response_model=ActivityCreate,)
def update_activity(
    activity_id: int,
    activity: ActivityCreate,
    session: Session = Depends(get_session)
):
    db_activity = session.scalar(select(Activity).where(Activity.id == activity_id))
    if not db_activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Atividade não encontrada!'
        )
    db_project = session.scalar(select(Project).where(Project.id == activity.project_id))
    if not db_project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Projeto não encontrado!'
        )
    db_activity.name = activity.name
    db_activity.description_activity = activity.description_activity
    db_activity.project_id = activity.project_id
    session.commit()
    session.refresh(db_activity)

    return db_activity


@router.delete('/{activity_id}', response_model=Message)
def delete_activity(
    activity_id: int,
    session: Session = Depends(get_session)
):
    db_activity = session.scalar(select(Activity).where(Activity.id == activity_id))
    if not db_activity:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Atividade não encontrada!'
        )
    session.delete(db_activity)
    session.commit()
    return {'message': 'Atividade deletada!'}
