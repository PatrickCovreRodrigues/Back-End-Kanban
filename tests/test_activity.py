from http import HTTPStatus


def test_create_activity(create_activity):
    assert create_activity.status_code == HTTPStatus.CREATED


def test_project_not_found(client, create_project):
    activity_creat = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 3,
        'status': 'PENDING'
    }
    response = client.post('/activitys', json=activity_creat)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não existe!'}


def test_read_all_activity(client, create_activity):
    with client as c:
        response = c.get('/activitys')
        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0


def test_read_all_activity_not_found(client):
    with client as c:
        response = c.get('/activitys')
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json() == {'detail': 'Não existe atividades!'}


def test_put_activity_not_found(client):
    activity_data = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 1,
        'status': 'PENDING'
    }
    response = client.put('/activitys/2', json=activity_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Atividade não encontrada!'}


def test_put_project_not_found(client, create_activity):
    second_activity_data = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 1,
        'status': 'PENDING'
    }
    response = client.post('/activitys', json=second_activity_data)

    activity_data = {
        'id': 1,
        'name': 'Teste Atualizado',
        'description_activity': 'Alguma coisa atualizada!',
        'project_id': 4,
        'status': 'PENDING'
    }
    response = client.put('/activitys/1', json=activity_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não encontrado!'}


def test_update_activity(client, create_activity):
    put_activity_data = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 1,
        'status': 'PENDING'
    }

    response = client.put(f'/activitys/{create_activity.json()['id']}', json=put_activity_data)
    assert response.status_code == HTTPStatus.OK

    put_activity = response.json()
    assert put_activity['id'] == put_activity_data['id']
    assert put_activity['name'] == put_activity_data['name']
    assert put_activity['description_activity'] == put_activity_data['description_activity']
    assert put_activity['project_id'] == put_activity_data['project_id']


def test_return_activity(client, create_activity):
    activity_id = 1
    response = client.get(f'/activitys/{activity_id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': activity_id,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 1,
        'status': 'PENDING',
        'created_at': response.json()['created_at']
    }


def test_activity_not_found(client, create_activity):
    response = client.get('/activitys/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Atividade não encontrada!'}


def test_delete_activity_not_found(client, create_activity):
    response = client.delete('/activitys/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Atividade não encontrada!'}


def test_delete_activity_ok(client, create_activity):
    response = client.delete('/activitys/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Atividade deletada!'}
