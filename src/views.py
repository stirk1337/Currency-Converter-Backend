import aiohttp
import redis_client


async def pong(request):
    return aiohttp.web.json_response({'status': 'OK', 'answer': 'pong'})


async def update(request):
    try:
        merge = int(request.query['merge'])
        if not merge:
            redis_client.clear_all()
        else:
            redis_client.update_currency()
        return aiohttp.web.json_response({'status': 'OK'})
    except (KeyError, ValueError):
        return aiohttp.web.json_response({'status': 'Something went wrong'})


async def convert(request):
    try:
        from_ = request.query['from']
        to = request.query['to']
        amount = request.query['amount']
        return aiohttp.web.json_response({'status': 'OK',   'answer': round(redis_client.convert(from_, to, amount), 2)})
    except (KeyError, ValueError):
        return aiohttp.web.json_response({'status': 'Something went wrong'})
