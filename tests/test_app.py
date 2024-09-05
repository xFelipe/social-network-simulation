import pytest


@pytest.mark.asyncio
async def test_root_must_return_ok_and_ola_mundo(context):
    response = context.client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá mundo!"}
