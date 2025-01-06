from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from fast_zero.models.database import get_session
from fast_zero.models.model import User
from fast_zero.schemas.schema_customers import CustomerCreate, CustomerRead
from fast_zero.schemas.schema_message import Message

router = APIRouter(
    prefix='/customers',
    tags=['customers'],
)


@router.post('/', status_code=HTTPStatus.CREATED, response_model=CustomerRead)
def customer_registration(customer: CustomerCreate, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.email == customer.email)
        )
    )

    if db_user:
        if db_user.email == customer.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Email já existe!'
            )
    new_customer = User(
        name=customer.name,
        email=customer.email,
        description=customer.description
    )
    session.add(new_customer)
    session.commit()
    session.refresh(new_customer)

    return new_customer


@router.get('/', response_model=List[CustomerRead])
def read_all_customers(session: Session = Depends(get_session)):
    db_user = session.execute(select(User)).scalars().all()
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Não existe clientes!'
        )

    return db_user


@router.get('/{customer_id}', response_model=CustomerCreate)
def read_customer(customer_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == customer_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado!'
        )

    return db_user


@router.put('/{customer_id}', response_model=CustomerCreate)
def update_customer(
    customer_id: int,
    customer: CustomerCreate,
    session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == customer_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado!'
        )
    try:
        db_user.name = customer.name
        db_user.email = customer.email
        db_user.description = customer.description
        session.commit()
        session.refresh(db_user)

        return db_user
    except IntegrityError as exc:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Email já existe!'
        ) from exc


@router.delete('/{customer_id}', response_model=Message)
def delete_customer(
    customer_id: int,
    session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == customer_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Cliente não encontrado!'
        )
    session.delete(db_user)
    session.commit()
    return {'message': 'Cliente deletado!'}
