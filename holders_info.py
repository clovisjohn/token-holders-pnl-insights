import csv
import pandas as pd
from api_requests import send_query, get_dexscreener_price_usd
from queries import query_sales, query_buys

def get_results(address_list, pair_address, progress_callback):
    results = []
    price_usd = get_dexscreener_price_usd(pair_address)
    for index, address in enumerate(address_list):
        sales_response = send_query(query_sales, address, pair_address)
        buys_response = send_query(query_buys, address, pair_address)

        amount0In_sum = sum([float(swap["amount0In"]) for swap in sales_response["data"]["pair"]["swaps"]])
        amountUSD_sum = sum([float(swap["amountUSD"]) for swap in sales_response["data"]["pair"]["swaps"]])

        amount0Out_sum = sum([float(swap["amount0Out"]) for swap in buys_response["data"]["pair"]["swaps"]])
        amountUSD_buy_sum = sum([float(swap["amountUSD"]) for swap in buys_response["data"]["pair"]["swaps"]])

        item = {
            "address": address,
            "amountBuy": round(amount0Out_sum,2),
            "purchaseUSDAmount": round(amountUSD_buy_sum,2),
            "amountSold": round(amount0In_sum,2),
            "saleUSDamount": round(amountUSD_sum,2)
        }
        item["remainingTokens"] = item["amountBuy"] - item["amountSold"]
        item["remainingTokensWorth"] = round(item["remainingTokens"] * price_usd,2)
        item["PNL"] = int(item["saleUSDamount"] + item["remainingTokensWorth"] - item["purchaseUSDAmount"])
        
        results.sort(key=lambda x: x["remainingTokensWorth"], reverse=True)
        results.append(item)
        progress_callback(index + 1)

    return results


