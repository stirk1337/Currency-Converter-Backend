import pytest
import redis
import requests

redis_client = redis.Redis('redis_service', 6379, 0)


def test_db():
    redis_client.set('SOME KEY', 'SOME VALUE')
    assert redis_client.get('SOME KEY').decode('utf-8') == 'SOME VALUE'
    redis_client.delete('SOME KEY')


def test_ping_route():
    answer = requests.get('http://localhost:8080/ping').json()
    assert answer['status'] == 'OK'
    assert answer['answer'] == 'pong'


def test_merge_equals_zero():
    answer = requests.post('http://localhost:8080/database?merge=0').json()
    assert answer['status'] == 'OK'


def test_merge_equals_one():
    answer = requests.post('http://localhost:8080/database?merge=1').json()
    assert answer['status'] == 'OK'


def test_2_eur_to_rur():
    answer = requests.get(
        'http://localhost:8080/convert?from=EUR&to=RUR&amount=2').json()
    assert answer['status'] == 'OK'
    assert type(answer['answer']) == float


def test_wrong_url():
    tests = [
        ('POST', 'http://localhost:8080/database?me'),
        ('POST', 'http://localhost:8080/database?merge='),
        ('GET', 'http://localhost:8080/convert?from=2'),
        ('GET', 'http://localhost:8080/convert?from=EUR&to=RUR&amount=meow'),
    ]
    for method, url in tests:
        if method == 'POST':
            answer = requests.post(url).json()
        else:
            answer = requests.get(url).json()
        print(answer)
        assert answer['status'] == 'Something went wrong'


def test_merge_equals_zero_again():
    answer = requests.post('http://localhost:8080/database?merge=0').json()
    assert answer['status'] == 'OK'


def run_tests():
    pytest.main()


if __name__ == '__main__':
    run_tests()
