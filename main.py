from aiohttp import web
from routes import routes

app = web.Application()
for route in routes:
    app.router.add_route(*route)

if __name__ == "__main__":
    web.run_app(app)
