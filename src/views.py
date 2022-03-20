import aiohttp

import src.redis_client


async def update_currency(request):
    try:
        merge = int(request.query['merge'])
        if not merge:
            src.redis_client.clear_all()
        else:
            src.redis_client.update_currency()
        return aiohttp.web.json_response({'status': 'OK'})
    except (KeyError, ValueError):
        return aiohttp.web.json_response({'status': 'Something went wrong'})


async def convert(request):
    try:
        from_ = request.query['from']
        to = request.query['to']
        amount = request.query['amount']
        return aiohttp.web.json_response(
            {'status': 'OK',
             'answer': round(src.redis_client.convert(from_, to, amount), 2)})
    except (KeyError, ValueError):
        return aiohttp.web.json_response({'status': 'Something went wrong'})
