import aiohttp
import pytest


HOST = 'localhost'
PORT = '8080'
MAIN_URL = f'http://{HOST}:{PORT}/'


@pytest.mark.asyncio
async def test_merge_equals_zero():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'database?merge=0'
        async with session.post(url) as response:
            assert response.status == 200
            answer = await response.json(content_type=None)
            assert answer['status'] == 'OK'


@pytest.mark.asyncio
async def test_merge_equals_one():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'database?merge=1'
        async with session.post(url) as response:
            assert response.status == 200
            answer = await response.json(content_type=None)
            assert answer['status'] == 'OK'


@pytest.mark.asyncio
async def test_merge_equals_one_get():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'database?merge=1'
        async with session.get(url) as response:
            assert response.status == 405

@pytest.mark.asyncio
async def test_2_eur_to_rur():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'convert?from=EUR&to=RUR&amount=2'
        async with session.get(url) as response:
            assert response.status == 200
            answer = await response.json(content_type=None)
            assert answer['status'] == 'OK'
            assert type(answer['answer']) == float


@pytest.mark.asyncio
async def test_2_eur_to_rur_post():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'convert?from=EUR&to=RUR&amount=2'
        async with session.post(url) as response:
            assert response.status == 405


@pytest.mark.asyncio
async def test_wrong_url_for_database_route():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'database?me'
        async with session.post(url) as response:
            assert response.status == 422


@pytest.mark.asyncio
async def test_wrong_url_for_convert_route_get():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'convert?xd'
        async with session.get(url) as response:
            assert response.status == 422

@pytest.mark.asyncio
async def test_wrong_url_for_convert_route_post():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'convert?xd'
        async with session.post(url) as response:
            assert response.status == 405

@pytest.mark.asyncio
async def test_wrong_server_url():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'datab'
        async with session.get(url) as response:
            assert response.status == 404


@pytest.mark.asyncio
async def test_merge_equals_zero_again():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'database?merge=0'
        async with session.post(url) as response:
            assert response.status == 200
            answer = await response.json(content_type=None)
            assert answer['status'] == 'OK'


@pytest.mark.asyncio
async def test_2_eur_to_rur_with_empty_database():
    async with aiohttp.ClientSession() as session:
        url = MAIN_URL + 'convert?from=EUR&to=RUR&amount=2'
        async with session.get(url) as response:
            assert response.status == 422


def run_tests():
    pytest.main()


if __name__ == '__main__':
    run_tests()
