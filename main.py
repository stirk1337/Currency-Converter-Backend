from aiohttp import web

from src.routes import routes

from src.redis_client import redis_middleware


def setup():
    app = web.Application(middlewares=[redis_middleware])
    for route in routes:
        app.router.add_route(*route)
    return app


def main():
    web.run_app(setup())


if __name__ == '__main__':
    main()
