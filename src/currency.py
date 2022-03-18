import asyncio
import aiohttp_requests
import nest_asyncio


async def request():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = await aiohttp_requests.requests.get(url)
    data = await response.json(content_type=None)
    return data


def get_currency_based_on_rur():
    nest_asyncio.apply()
    data = asyncio.run(request())
    curs_list = []
    curs_value = {}
    for currencies in data['Valute']:
        curs_list.append(currencies)
        cur = data['Valute'][currencies]
        curs_value[currencies] = cur['Value'] / cur['Nominal']
    pairs = {}
    for i in range(len(curs_list)):
        pairs[curs_list[i] + 'RUR'] = curs_value[curs_list[i]]
        for j in range(len(curs_list)):
            pairs[curs_list[i] + curs_list[j]
                  ] = curs_value[curs_list[i]] / curs_value[curs_list[j]]
    return pairs


if __name__ == '__main__':
    from base_logger import logger
    logger.debug(get_currency_based_on_rur())

