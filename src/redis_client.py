import aioredis
from src.currency import get_currency_based_on_rur
import contextvars

REDIS_URL = 'redis://redis_service:6379'
redis_var = contextvars.ContextVar('redis_var')


class RedisClient():
    async def async_init(self):
        self.redis = await aioredis.from_url(REDIS_URL,
                                             encoding="utf-8",
                                             decode_responses=True)

    async def clear_all(self):
        async with self.redis.client() as conn:
            await conn.flushall()

    async def update_currency(self):
        data = await get_currency_based_on_rur()
        async with self.redis.client() as conn:
            for value in data:
                await conn.set(value, data[value])

    async def convert(self, from_, to, amount):
        async with self.redis.client() as conn:
            data = await conn.get(from_ + to)
            data_reverse = await conn.get(to + from_)
            if data is not None:
                return float(data) * float(amount)
            elif data_reverse is not None:
                return 1/float(data_reverse) * float(amount)
            else:
                raise KeyError
