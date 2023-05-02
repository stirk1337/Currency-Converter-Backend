import aiohttp
import json


async def get_cbr_currency():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        async with session.get(url) \
                as response:
            data = json.loads(await response.read())
            return data


async def get_currency_based_on_rur():
    data = await get_cbr_currency()
    pairs = {}
    for currency in data['Valute']:
        nominal = data['Valute'][currency]['Nominal']
        value = data['Valute'][currency]['Value'] / nominal
        pairs[currency + 'RUR'] = value
        for currency2 in data['Valute']:
            if currency != currency2:
                nominal2 = data['Valute'][currency2]['Nominal']
                value2 = data['Valute'][currency2]['Value'] / nominal2
                pairs[currency + currency2] = value / value2
    return pairs
