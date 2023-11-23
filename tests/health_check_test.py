import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_health_check(async_client: AsyncClient) -> dict:
    response = await async_client.get("/items/5?q=somequery")
    expected = {"item_id": 5, "q": "somequery"}
    assert response.status_code == 200
    assert response.json() == expected


@pytest.mark.anyio
async def test_root(async_client: AsyncClient) -> dict:
    response = await async_client.get("/")
    expected = {"Hello": "World"}
    assert response.status_code == 200
    x = response.json()
    assert expected.items() <= x.items()


# async def create_post(body: str, async_client: AsyncClient) -> dict:
#     response = await async_client.post("/post", json={"body": body})
#     return response.json()


# async def create_comment(body: str, post_id: int, async_client: AsyncClient) -> dict:
#     response = await async_client.post(
#         "/comment", json={"body": body, "post_id": post_id}
#     )
#     return response.json()


# @pytest.fixture()
# async def created_post(async_client: AsyncClient):
#     return await create_post("Test post", async_client)


# @pytest.mark.anyio
# async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
#     response = await async_client.get("/post")
#     assert response.status_code == 200
#     assert response.json() == [created_post]
