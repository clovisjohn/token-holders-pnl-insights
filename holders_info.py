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
            "holder": address,
            "Purchase amount": round(amount0Out_sum,2),
            "Purchase amount (USD)": round(amountUSD_buy_sum,2),
            "Sale amount": round(amount0In_sum,2),
            "Sale amount (USD)": round(amountUSD_sum,2)
        }
        item["Remaining Tokens"] = item["Purchase amount"] - item["Sale amount"]

        if item["Remaining Tokens"] < 0 :
            item["Remaining Tokens"] = 0;
            
        item["Remaining Tokens Worth"] = round(item["Remaining Tokens"] * price_usd,2)
        item["PNL"] = int(item["Sale amount (USD)"] + item["Remaining Tokens Worth"] - item["Purchase amount (USD)"]) # not exactly pnl
        
        results.append(item)
        progress_callback(index + 1)  

    results.sort(key=lambda x: x["Remaining Tokens Worth"], reverse=True)
    return results


