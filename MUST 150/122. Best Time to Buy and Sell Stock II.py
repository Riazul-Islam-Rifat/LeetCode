class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        # Valley peak approach.
        for price in range(1,len(prices)):
            # Next day selling price is higher than previous day's buying price
            if prices[price] > prices[price-1]:
                profit+= prices[price] - prices[price-1]

        return profit

    # Time complexity: O(N)
    # Space complexity: O(1)