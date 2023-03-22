query_sales = """
    query MyQuery($from: String!, $pairAddress: Bytes!) {
        pair(id: $pairAddress) {
            swaps(
                orderDirection: desc
                orderBy: timestamp
                where: {amount1In: "0", from: $from}
            ) {
                amount0In
                amountUSD
                from
            }
        }
    }
"""

query_buys = """
    query MyQuery($from: String!, $pairAddress: Bytes!) {
        pair(id: $pairAddress) {
            swaps(
                orderDirection: desc,
                orderBy: timestamp,
                where: {amount1Out: "0", from: $from}
            ) {
                amount0Out
                amountUSD
                from
            }
        }
    }
"""

