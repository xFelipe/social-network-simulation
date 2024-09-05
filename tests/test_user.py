import pytest


@pytest.mark.asyncio
async def test_create_user_1(context):
    response = context.client.post("/api/v1/user", json=user_1)
    content = response.json()
    assert response.status_code == 201, content
    assert content == user_1_public


@pytest.mark.asyncio
async def test_cant_create_user_with_same_username_1(context):
    user_with_same_username = user_2.copy()
    user_with_same_username["username"] = user_1["username"]

    await context.new_user(user_1)
    response = context.client.post("/api/v1/user", json=user_with_same_username)
    content = response.json()
    assert response.status_code == 400, content


@pytest.mark.asyncio
async def test_get_user(context):
    await context.new_user(user_1)
    response = context.client.get("/api/v1/user/1")
    content = response.json()
    assert response.status_code == 200, response.json()
    assert content == user_1_public


@pytest.mark.asyncio
async def test_get_non_existent_user(context):
    response = context.client.get("/api/v1/user/150")
    assert response.status_code == 404, response.json()


@pytest.mark.asyncio
async def test_get_all_users(context):
    client = context.client
    await context.new_user(user_1)
    await context.new_user(user_2)
    response = client.get("/api/v1/user")
    assert response.json() == [user_1_public, user_2_public], response.json()


@pytest.mark.asyncio
async def test_update_user(context):
    context.client.post("/api/v1/user", json=user_1)
    response = context.client.put("/api/v1/user/1", json=user_1_update)
    assert response.status_code == 200, response.json()
    assert response.json() == user_1_update_public, response.json()


@pytest.mark.asyncio
async def test_delete_user(context):
    await context.new_user(user_1)
    response = context.client.delete("/api/v1/user/1")
    all_users = await context.get_list_users()
    assert len(all_users) == 0, response.content


user_1 = {
    "name": "Nome1",
    "username": "Username1",
    "password": "12345678",
    "birthday": "1998-02-25",
    "sex": "outro",
}
user_1_public = {
    "id": 1,
    "name": "Nome1",
    "username": "Username1",
    "birthday": "1998-02-25",
    "sex": "outro",
}
user_1_update = {
    "name": "Nome111",
    "username": "Username111",
    "sex": "masculino",
}
user_1_update_public = {
    "id": 1,
    "name": "Nome111",
    "username": "Username111",
    "birthday": "1998-02-25",
    "sex": "masculino",
}
user_2 = {
    "name": "Nome2",
    "username": "Username2",
    "password": "87654321",
    "birthday": "1997-02-26",
    "sex": "masculino",
}
user_2_public = {
    "id": 2,
    "name": "Nome2",
    "username": "Username2",
    "birthday": "1997-02-26",
    "sex": "masculino",
}
