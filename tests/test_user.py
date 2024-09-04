import pytest

new_user = {
    "name": "Nome1",
    "username": "Username1",
    "password": "12345678",
    "birthday": "1998-02-25",
    "sex": "outro",
}

changed_user = {
    "name": "Nome2",
    "username": "Username2",
    "birthday": "1998-02-26",
    "sex": "masculino",
}


@pytest.mark.asyncio
async def test_new_user(client):
    response = client.post("/api/v1/user", json=new_user)
    content = response.json()
    assert response.status_code == 201, content
    assert content == {
        "name": "Nome1",
        "username": "Username1",
        "password": "12345678",
        "birthday": "1998-02-25",
        "sex": "outro",
        "id": 1,
    }
