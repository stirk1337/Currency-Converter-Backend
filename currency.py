import urllib.request
import json


def get_currency_based_on_rur():
    with urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js") as url:
        data = json.loads(url.read())
        curs_list = []
        curs_value = {}
        for currencies in data['Valute']:
            curs_list.append(currencies)
            cur = data['Valute'][currencies]
            curs_value[currencies] = cur['Value']/cur['Nominal']
        pairs = {}
        for i in range(len(curs_list)):
            pairs[curs_list[i] + 'RUR'] = curs_value[curs_list[i]]
            for j in range(len(curs_list)):
                pairs[curs_list[i] + curs_list[j]] = curs_value[curs_list[i]] / curs_value[curs_list[j]]
        return pairs


if __name__ == "__main__":
    print(get_currency_based_on_rur())
