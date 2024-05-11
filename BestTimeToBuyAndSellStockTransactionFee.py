# I don't know why this is not working. It somehow explores all combinations in an effective way,
# because of the cache. I think it goes to all possibilities with just buy(0) but I don't know
# how it computes the max profit possible over multiple transactions.

class Solution(object):
    def maxProfit(self, prices, fee):
        N = len(prices)

        sell_cache = [None] * N
        buy_cache = [None] * N

        def buy(day):
            if day == N:
                return 0

            if buy_cache[day]:
                return buy_cache[day]

            buying = sell(day + 1) - (prices[day] + fee)
            not_buying = buy(day + 1)

            buy_cache[day] = max(buying, not_buying)

            return buy_cache[day]

        def sell(day):
            if day == N:
                return 0

            if sell_cache[day]:
                return sell_cache[day]

            selling = buy(day + 1) + prices[day]
            not_selling = sell(day + 1)

            sell_cache[day] = max(selling, not_selling)

            return sell_cache[day]