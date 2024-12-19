from http import HTTPStatus


def test_create_customer(create_customer):
    assert create_customer.status_code == HTTPStatus.CREATED


def test_read_customer(client, create_customer):
    response = client.get('/customers/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado!'}


def test_return_customer(client, create_customer):
    customer_id = 1
    response = client.get(f'/customers/{customer_id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': customer_id,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa!'
    }


def test_update_customers(client, create_customer):
    update_data = {
        'id': 1,
        'name': 't',
        'email': 't@gmail.com',
        'description': 't coisa!'
    }
    response = client.put('/customers/1', json=update_data)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == update_data


def test_update_not_found(client):
    customer_data = {
        'id': 2,
        'name': 'Nome',
        'email': 'novoemail@gmail.com',
        'description': 'descrição'
    }
    response = client.put('/customers/321', json=customer_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado!'}


def test_update_detail_email(client, create_customer):
    second_customer_data = {
        'id': 2,
        'name': 'teste',
        'email': 't@gmail.com',
        'description': ''
    }
    client.post('/customers', json=second_customer_data)

    customer_data = {
        'id': 2,
        'name': 'Cliente Atualizado',
        'email': 'Teste@gmail.com',
        'description': 'Descrição atualizada'
    }
    response = client.put('/customers/2', json=customer_data)
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email já existe!'}


def test_detail_email(client, create_customer):
    customer_data = {
        'id': 1,
        'name': 'Teste',
        'email': 'Teste@gmail.com',
        'description': 'Alguma coisa'
    }

    response = client.post('/customers', json=customer_data)
    assert response.status_code == HTTPStatus.CONFLICT  # se der erro coloca BAD_REQUEST
    assert response.json() == {'detail': 'Email já existe!'}


def test_delete_not_found(client, create_customer):
    response = client.delete('/customers/3')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado!'}


def test_delete_customer(client, create_customer):
    response = client.delete('/customers/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Cliente deletado!'}
