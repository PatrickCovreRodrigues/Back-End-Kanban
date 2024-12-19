from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from fast_zero.app import app
from fast_zero.models.database import get_session
from fast_zero.models.model import table_registry


@pytest.fixture
def client(session):
    def get_session_override():
        return session
    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client
    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
    table_registry.metadata.drop_all(engine)


@pytest.fixture
def create_customer(client):
    customer_data = {
        'id': 1,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa!'
    }
    response = client.post('/customers', json=customer_data)
    assert response.status_code == HTTPStatus.CREATED
    return response


@pytest.fixture
def create_project(client, create_customer):
    project_data = {
        'id': 1,
        'name': 'Teste',
        'description_project': 'Alguma coisa!',
        'customer_id': 1
    }
    response = client.post('/projects', json=project_data)
    assert response.status_code == HTTPStatus.CREATED
    return response
