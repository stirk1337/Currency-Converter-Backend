import redis
from currency import get_currency_based_on_rur

redis_client = redis.Redis("redis_service", 6379, 0)


def clear_all():
    redis_client.flushall()


def update_currency():
    data = get_currency_based_on_rur()
    for value in data:
        redis_client.set(value, data[value])


def convert(from_, to, amount):
    data = redis_client.get(from_ + to)
    data_reverse = redis_client.get(to + from_)
    print(data)
    if data is not None:
        return float(redis_client.get(from_ + to)) * float(amount)
    elif data_reverse is not None:
        return 1/float(redis_client.get(to + from_)) * float(amount)
    else:
        raise KeyError


if __name__ == "__main__":
    print(redis_client)

redis_client.close()
