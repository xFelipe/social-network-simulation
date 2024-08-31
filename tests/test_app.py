from fastapi import status


def test_root_must_return_ok_and_ola_mundo(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Olá mundo!"}
