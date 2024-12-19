from http import HTTPStatus


def test_create_activity(create_activity):
    assert create_activity.status_code == HTTPStatus.CREATED


def test_project_not_found(client, create_project):
    activity_creat = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 3
    }
    response = client.post('/activitys', json=activity_creat)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não existe!'}


def test_put_activity_not_found(client):
    activity_data = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 1
    }
    response = client.put('/activitys/2', json=activity_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Atividade não encontrada!'}


def test_put_project_not_found(client, create_activity):
    second_activity_data = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 1
    }
    response = client.post('/activitys', json=second_activity_data)

    activity_data = {
        'id': 1,
        'name': 'Teste Atualizado',
        'description_activity': 'Alguma coisa atualizada!',
        'project_id': 4
    }
    response = client.put('/activitys/1', json=activity_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não encontrado!'}


def test_activity_equals_conflict(client, create_activity):
    activity_creat = {
        'id': 1,
        'name': 'Teste',
        'description_activity': 'Alguma coisa!',
        'project_id': 1
    }
    response = client.post('/activitys', json=activity_creat)
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Atividade já existe!'}


def test_delete_activity_not_found(client, create_activity):
    response = client.delete('/activitys/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Atividade não encontrada!'}


def test_delete_activity_ok(client, create_activity):
    response = client.delete('/activitys/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Atividade deletada!'}
