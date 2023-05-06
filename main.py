from aiohttp import web
from src.routes import routes
from src.redis_client import RedisClient, redis_var


async def on_startup(app):
    redis = RedisClient()
    await redis.async_init()
    redis_var.set(redis)


async def on_cleanup(app):
    redis = redis_var.get()
    await redis.close()


def setup():
    app = web.Application()
    for route in routes:
        app.router.add_route(*route)
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)
    return app


def main():
    web.run_app(setup())


if __name__ == '__main__':
    main()
