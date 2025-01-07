from http import HTTPStatus


def test_create_project(create_project):
    assert create_project.status_code == HTTPStatus.CREATED


def test_customer_not_found(client, create_customer):
    project_creat = {
        'id': 1,
        'name': 'Teste',
        'description_project': 'Alguma coisa!',
        'customer_id': 3
    }
    response = client.post('/projects', json=project_creat)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não existe!'}


def test_project_all_not_found(client):
    response = client.get('/projects/')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Não existe projetos!'}


def test_return_get_projects(client, create_project):
    response = client.get('/projects/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {
            'customer_id': 1,
            'description_project': 'Alguma coisa!',
            'id': 1,
            'name': 'Teste',
            'created_at': response.json()[0]['created_at'],
        }
    ]


def test_update_project(client, create_project):
    project_data = {
        'id': 1,
        'name': 'Teste',
        'description_project': 'Alguma coisa!',
        'customer_id': 1
    }
    response = client.put(f'projects/{create_project.json()['id']}', json=project_data)
    assert response.status_code == HTTPStatus.OK

    put_project = response.json()
    assert put_project['name'] == project_data['name']
    assert put_project['description_project'] == project_data['description_project']
    assert put_project['customer_id'] == project_data['customer_id']


def test_return_project_get(client, create_project):
    project_id = 1
    response = client.get(f'/projects/{project_id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'customer_id': 1,
        'description_project': 'Alguma coisa!',
        'id': 1,
        'name': 'Teste',
        'created_at': response.json()['created_at'],
    }


def test_project_not_found(client, create_project):
    response = client.get('/projects/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não encontrado!'}


def test_put_project_not_found(client):
    project_data = {
        'id': 1,
        'name': 'Teste',
        'description_project': 'Alguma coisa!',
        'customer_id': 1
    }
    response = client.put('/projects/2', json=project_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não encontrado!'}


def test_put_customer_not_found(client, create_project):
    second_project_data = {
        'id': 2,
        'name': 'Teste',
        'description_project': 'Alguma coisa!',
        'customer_id': 1
    }
    client.post('/projects', json=second_project_data)

    project_data = {
        'id': 2,
        'name': 'Teste',
        'description_project': 'Alguma coisa!',
        'customer_id': 4
    }
    response = client.put('/projects/2', json=project_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado!'}


def test_delete_not_found(client, create_project):
    response = client.delete('/projects/3')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não encontrado!'}


def test_delete_customer(client, create_project):
    response = client.delete('/projects/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Projeto deletado!'}
