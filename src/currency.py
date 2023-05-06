import aiohttp
from pydantic import BaseModel
from typing import Dict


class CurrencyInfo(BaseModel):
    CharCode: str
    Nominal: int
    Name: str
    Value: float


class CBRData(BaseModel):
    Date: str
    PreviousDate: str
    PreviousURL: str
    Timestamp: str
    Valute: Dict[str, CurrencyInfo]


async def get_cbr_currency() -> CBRData:
    async with aiohttp.ClientSession() as session:
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        async with session.get(url) as response:
            data = await response.json(content_type='application/javascript')
            return CBRData(**data)


async def get_currency_based_on_rur() -> Dict[str, float]:
    data = await get_cbr_currency()
    pairs = {}

    for currency in data.Valute:
        nominal = data.Valute[currency].Nominal
        value = data.Valute[currency].Value / nominal
        pairs[currency + 'RUR'] = value

        for currency2 in data.Valute:
            if currency != currency2:
                nominal2 = data.Valute[currency2].Nominal
                value2 = data.Valute[currency2].Value / nominal2
                pairs[currency + currency2] = value / value2

    return pairs
