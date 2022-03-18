import aiohttp_requests
import pytest
import redis


redis_client = redis.Redis('redis_service', 6379, 0)


def test_db():
    redis_client.set('SOME KEY', 'SOME VALUE')
    assert redis_client.get('SOME KEY').decode('utf-8') == 'SOME VALUE'
    redis_client.delete('SOME KEY')


@pytest.mark.asyncio
async def test_ping_route():
    response = await aiohttp_requests.requests.get('http://localhost:8080/ping')
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'
    assert answer['answer'] == 'pong'


@pytest.mark.asyncio
async def test_merge_equals_zero():
    response = await aiohttp_requests.requests.post('http://localhost:8080/database?merge=0')
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'


@pytest.mark.asyncio
async def test_merge_equals_one():
    response = await aiohttp_requests.requests.post('http://localhost:8080/database?merge=1')
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'


@pytest.mark.asyncio
async def test_2_eur_to_rur():
    response = await aiohttp_requests.requests.get(
        'http://localhost:8080/convert?from=EUR&to=RUR&amount=2')
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'
    assert type(answer['answer']) == float


@pytest.mark.asyncio
async def test_wrong_url():
    tests = [
        ('POST', 'http://localhost:8080/database?me'),
        ('POST', 'http://localhost:8080/database?merge='),
        ('GET', 'http://localhost:8080/convert?from=2'),
        ('GET', 'http://localhost:8080/convert?from=EUR&to=RUR&amount=meow'),
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
    response = await aiohttp_requests.requests.post('http://localhost:8080/database?merge=0')
    answer = await response.json(content_type=None)
    assert answer['status'] == 'OK'


def run_tests():
    pytest.main()


if __name__ == '__main__':
    run_tests()
