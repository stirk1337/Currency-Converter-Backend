import time
from aiohttp import web
from routes import routes
import threading
import test_api


def setup():
    app = web.Application()
    for route in routes:
        app.router.add_route(*route)
    return app


def testing():
    time.sleep(1)  # wait for app to start
    test_api.run_tests()


def main():
    threading.Thread(target=testing).start()
    web.run_app(setup())


if __name__ == "__main__":
    main()
