import requests

def send_query(query, from_address, pair_address):
    request_data = {
        "operationName": "pair",
        "query": query,
        "variables": {"from": from_address, "pairAddress": pair_address}
    }
    headers = {
        'Content-Type': 'application/json',
    }
    endpoint = "https://api.thegraph.com/subgraphs/name/camelotlabs/camelot-amm"
    response = requests.post(endpoint, json=request_data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {response.text}")

def get_dexscreener_price_usd(pair_address):
    dexscreener_url = f"https://api.dexscreener.com/latest/dex/pairs/arbitrum/{pair_address}"
    dexscreener_response = requests.get(dexscreener_url)
    price_usd = float(dexscreener_response.json()['pairs'][0]['priceUsd'])
    return price_usd

