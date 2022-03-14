import aiohttp
from aiohttp import web


async def handle(request):
    return aiohttp.web.json_response({'status': 'success'})


async def print(request):
    try:
        message = request.query['message']
        message2 = request.query['message2']
        message3 = request.query['message3']
        return aiohttp.web.json_response({'message': message, 'message2': message2, 'message3': message3})
    except:
        return aiohttp.web.json_response("you did something wrong")

app = web.Application()

app.router.add_get('/', handle)
app.router.add_post('/print', print)

web.run_app(app)
