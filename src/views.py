import aiohttp
from pydantic import BaseModel, validator, ValidationError
from src.redis_client import redis_var


class MergeRequest(BaseModel):
    merge: int

    @validator('merge')
    def validate_merge(cls, v):
        if v not in [0, 1]:
            raise ValueError('Invalid value for merge parameter')
        return v


async def update_currency(request):
    try:
        merge_request = MergeRequest(merge=request.query.get('merge'))
    except (ValueError, ValidationError):
        raise aiohttp.web.HTTPUnprocessableEntity(
                reason='Invalid value for merge parameter'
        )
    redis_client = redis_var.get()
    if merge_request.merge == 0:
        await redis_client.clear_all()
    else:
        await redis_client.update_currency()
    return aiohttp.web.json_response({'status': 'OK'})


class ConvertRequest(BaseModel):
    from_: str
    to: str
    amount: float


async def convert(request):
    try:
        convert_request = ConvertRequest(
            from_=request.query.get('from'),
            to=request.query.get('to'),
            amount=request.query.get('amount')
        )
    except (ValidationError):
        raise aiohttp.web.HTTPUnprocessableEntity(
                reason='Invalid value for from, to, amount parameters'
        )
    redis_client = redis_var.get()
    try:
        answer = await redis_client.convert(
            convert_request.from_,
            convert_request.to,
            convert_request.amount
        )
    except (KeyError):
        raise aiohttp.web.HTTPUnprocessableEntity(reason='Database is empty')

    return aiohttp.web.json_response({'status': 'OK',
                                      'answer': round(answer, 2)})
