# from http import HTTPStatus


# def test_create_activity(client):
#     client.post(
#         '/customers',
#         json={
#             'id': 1,
#             'name': 'Cliente Teste',
#             'email': 'cliente@teste.com',
#             'description': 'Cliente para teste',
#         }
#     )

#     response = client.post(
#         '/activity/',
#         json={
#             'id': 1,
#             'name': 'Atividade Teste',
#             'description_activity': 'Descrição da atividade de teste',
#             'customer_id': 1,
#         }
#     )

#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json() == {
#         'id': 1,
#         'name': 'Atividade Teste',
#         'description_activity': 'Descrição da atividade de teste',
#         'customer_id': 1,
#     }


# def test_not_customer_activity(client):
#     client.post(
#         '/customers',
#         json={
#             'id': 1,
#             'name': 'Cliente Teste',
#             'email': 'cliente@teste.com',
#             'description': 'Cliente para teste',
#         }
#     )

#     response = client.post(
#         '/activity/',
#         json={
#             'id': 1,
#             'name': 'Atividade Teste',
#             'description_activity': 'Descrição da atividade de teste',
#             'customer_id': 2,
#         }
#     )

#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json() == {
#         'id': 1,
#         'name': 'Atividade Teste',
#         'description_activity': 'Descrição da atividade de teste',
#         'customer_id': 1,
#     }


# def test_read_activity(client):
#     client.post(
#         '/customers',
#         json={
#             'id': 1,
#             'name': 'Cliente Teste',
#             'email': 'cliente@teste.com',
#             'description': 'Cliente para teste',
#         }
#     )
#     client.post(
#         '/activity/',
#         json={
#             'id': 1,
#             'name': 'Atividade Teste',
#             'description_activity': 'Descrição da atividade de teste',
#             'customer_id': 1,
#         }
#     )

#     response = client.get('/activity/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'id': 1,
#         'name': 'Atividade Teste',
#         'description_activity': 'Descrição da atividade de teste',
#         'customer_id': 1,
#     }


# def test_update_activity(client):
#     client.post(
#         '/customers',
#         json={
#             'id': 1,
#             'name': 'Cliente Teste',
#             'email': 'cliente@teste.com',
#             'description': 'Cliente para teste',
#         }
#     )

#     response = client.post(
#         '/activity/',
#         json={
#             'id': 1,
#             'name': 'Atividade Teste',
#             'description_activity': 'Descrição da atividade de teste',
#             'customer_id': 1,
#         }
#     )

#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json() == {
#         'id': 1,
#         'name': 'Atividade Teste',
#         'description_activity': 'Descrição da atividade de teste',
#         'customer_id': 1,
#     }

#     response = client.put(
#         '/activity/1',
#         json={
#             'id': 1,
#             'name': 'Te',
#             'description_activity': 'Testado!',
#             'customer_id': 1
#         }
#     )
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'id': 1,
#         'name': 'Te',
#         'description_activity': 'Testado!',
#         'customer_id': 1
#     }


# def test_delete_activity(client):
#     client.post(
#         '/customers',
#         json={
#             'id': 1,
#             'name': 'Cliente Teste',
#             'email': 'cliente@teste.com',
#             'description': 'Cliente para teste',
#         }
#     )

#     response = client.post(
#         '/activity/',
#         json={
#             'id': 1,
#             'name': 'Atividade Teste',
#             'description_activity': 'Descrição da atividade de teste',
#             'customer_id': 1,
#         }
#     )

#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json() == {
#         'id': 1,
#         'name': 'Atividade Teste',
#         'description_activity': 'Descrição da atividade de teste',
#         'customer_id': 1,
#     }

#     response = client.delete('/activity/1')

#     assert response.status_code == HTTPStatus.OK
