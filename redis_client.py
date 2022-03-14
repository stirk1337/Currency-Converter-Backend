import redis
from currency import get_currency_based_on_rur

redis_client = redis.Redis("localhost", 6379, 0)


def clear_all():
    redis_client.flushall()


def update_currency():
    data = get_currency_based_on_rur()
    for value in data:
        redis_client.set(value, data[value])


def convert(from_, to, amount):
    return float(redis_client.get(from_ + to)) * float(amount)


redis_client.close()
