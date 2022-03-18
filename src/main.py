from aiohttp import web

from routes import routes


def setup():
    app = web.Application()
    for route in routes:
        app.router.add_route(*route)
    return app


def main():
    web.run_app(setup())


if __name__ == '__main__':
    main()
