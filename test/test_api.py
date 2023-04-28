import aiohttp_requests
import pytest
import redis

redis_client = redis.Redis('localhost', 6379, 0)

host = 'localhost'
port = '8080'
main_url = f'http://{host}:{port}/'

@pytest.mark.asyncio
async def test_merge_equals_zero():
    url = main_url + 'database?merge=0'
    response = await aiohttp_requests.requests.post(url)
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'


@pytest.mark.asyncio
async def test_merge_equals_one():
    url = main_url + 'database?merge=1'
    response = await aiohttp_requests.requests.post(url)
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'


@pytest.mark.asyncio
async def test_2_eur_to_rur():
    url = main_url + 'convert?from=EUR&to=RUR&amount=2'
    response = await aiohttp_requests.requests.get(url)
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'
    assert type(answer['answer']) == float


@pytest.mark.asyncio
async def test_wrong_url():
    tests = [
        ('POST', main_url + 'database?me'),
        ('POST', main_url + 'database?merge='),
        ('GET', main_url + 'convert?from=2'),
        ('GET', main_url + 'convert?from=EUR&to=RUR&amount=meow'),
    ]
    for method, url in tests:
        if method == 'POST':
            response = await aiohttp_requests.requests.post(url)
        else:
            response = await aiohttp_requests.requests.get(url)
        answer = await response.json(content_type=None)
        assert answer['status'] == 'Something went wrong'


@pytest.mark.asyncio
async def test_merge_equals_zero_again():
    url = url = main_url + 'database?merge=0'
    response = await aiohttp_requests.requests.post(url)
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'


def run_tests():
    pytest.main()


if __name__ == '__main__':
    run_tests()
