from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_prices(summary) -> "dict {name: latest price} for the coins in summary ":
    ids = get_ids(summary)
    current_prices = {}
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'id': ids,
        'convert': 'USD',
        'aux': "is_fiat"
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'dc7be161-4862-4613-9d8c-ea6521e7f907',
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    else:

        # extract the prices from json data
        for key, value in data["data"].items():
            name = value["name"].lower()
            quote = value["quote"]
            for k, v in quote.items():
                current_prices.update({name: v["price"]})
        return current_prices


def get_ids(summary):
    matched_ids = update_ids(summary)
    ids = ""
    for coin in matched_ids:
        ids += f"{coin['id']},"
    return ids[:-1]


def update_ids(summary):
    symbols = get_symbols(summary)
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
        'symbol': symbols,
        'aux': "is_active",
        'sort': "id"

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'dc7be161-4862-4613-9d8c-ea6521e7f907',
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    else:
        return match_ids(summary, data)


def get_symbols(summary):
    # create a comma separated concatenation of symbols
    symbols = ""
    for coin in summary:
        symbols += f"{coin['symbol']},"
    return symbols[:-1]


def match_ids(summary: list, data: dict):
    data_copy = data["data"]
    matched_ids = []
    matched_names = set()
    matched_symbols = set()
    for i in summary:
        for j in data_copy:
            j_name = j["name"].lower()
            j_symbol = j["symbol"].lower()
            matched_names.add(j_name)
            if i["symbol"] == j_symbol and i["name"] == j_name:
                matched_ids.append({"id": j["id"], "name": j_name, "symbol": j_symbol})
                matched_symbols.add(j_symbol)
            if j_symbol in matched_symbols:
                data_copy.pop(data_copy.index(j))

    if len(summary) != len(matched_ids):
        errors = name_errors(summary, matched_names, data_copy)
        raise KeyError(errors)
    return matched_ids


def name_errors(summary, matched_names, data_copy):
    correct_names = []
    unmatched_names = ""
    for i in summary:
        if i["name"] not in matched_names:
            unmatched_names += f'{i["name"]}, '
            for j in data_copy:
                if j["symbol"].lower() == i["symbol"]:
                    correct_names.append({j["symbol"].lower(): j["slug"]})
    if len(correct_names) != 0:
        return f'invalid symbol/name for {unmatched_names} found: {correct_names}'





