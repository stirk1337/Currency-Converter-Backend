import aioredis
from src.currency import get_currency_based_on_rur

REDIS_URL = 'redis://redis_service:6379'


async def clear_all():
    redis = aioredis.from_url(
        REDIS_URL, encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        await conn.flushall()


async def update_currency():
    redis = aioredis.from_url(
        REDIS_URL, encoding="utf-8", decode_responses=True
    )
    data = await get_currency_based_on_rur()
    async with redis.client() as conn:
        for value in data:
            await conn.set(value, data[value])


async def convert(from_, to, amount):
    redis = aioredis.from_url(
        REDIS_URL, encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        data = await conn.get(from_ + to)
        data_reverse = await conn.get(to + from_)
        if data is not None:
            return float(await conn.get(from_ + to)) * float(amount)
        elif data_reverse is not None:
            return 1/float(await conn.get(to + from_)) * float(amount)
        else:
            raise KeyError
