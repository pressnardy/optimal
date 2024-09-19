import cmc_api
data = {'status':
     {'timestamp': '2023-09-14T06:38:45.638Z', 'error_code': 0, 'error_message': None, 'elapsed': 8, 'credit_count': 1, 'notice': None},
 'data': [{'id': 2010, 'rank': 7, 'name': 'Cardano', 'symbol': 'ADA', 'slug': 'cardano', 'is_active': 1, 'platform': None},
          {'id': 1027, 'rank': 2, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'is_active': 1, 'platform': None},
          {'id': 5426, 'rank': 9, 'name': 'Solana', 'symbol': 'SOL', 'slug': 'solana', 'is_active': 1, 'platform': None},
          {'id': 16116, 'rank': 2129, 'name': 'Wrapped Solana', 'symbol': 'SOL', 'slug': 'wrapped-solana', 'is_active': 1, 'platform': {'id': 16, 'name': 'Solana', 'symbol': 'SOL', 'slug': 'solana', 'token_address': 'So11111111111111111111111111111111111111112'}},
          {'id': 591, 'rank': None, 'name': 'Solcoin', 'symbol': 'SOL', 'slug': 'solcoin', 'is_active': 0, 'platform': None},
          {'id': 3333, 'rank': None, 'name': 'Sola Token', 'symbol': 'SOL', 'slug': 'sola-token', 'is_active': 0, 'platform': {'id': 1, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'token_address': '0x1f54638b7737193ffd86c19ec51907a7c41755d8'}},
          {'id': 12003, 'rank': None, 'name': 'SOL RUNE - Rune.Game', 'symbol': 'SOL', 'slug': 'sol-rune---rune-game', 'is_active': 0, 'platform': {'id': 14, 'name': 'BNB Smart Chain (BEP20)', 'symbol': 'BNB', 'slug': 'bnb', 'token_address': '0x4ffd3b8ba90f5430cda7f4cc4c0a80df3cd0e495'}}
          ]
 }

summary = [
        {"name": "cardano", "symbol": "ada", "risk score": 3, "balance": 200, "investment": 100},
        {"name": "ethereum", "symbol": "eth", "risk score": 4, "balance": 0.25, "investment": 500},
        {"name": "solana", "symbol": "sol", "risk score": 2, "balance": 20, "investment": 200},
        {"name": "the sandbox", "symbol": "sand", "risk score": 1, "balance": 50, "investment": 100},
    ]


coin_summary = [{
    "name": "the sandbox",
    "symbol": "sand",
    "risk_score": 1,
    "balance": 50,
    "investment": 100,
}]

# matched_names = {"ethereum", "cardano", "solana"}

print(cmc_api.get_prices(summary))


results = {
    'ethereum': 1636.299150295787,
    'cardano': 0.2508419897851198,
    'solana': 19.123171829451113,
    'the sandbox': 0.3076233743271176
}

"""
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


print(name_errors(summary, matched_names, data["data"]))
"""








