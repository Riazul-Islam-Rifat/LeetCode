class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # Here we are going to use the sliding window approach [Two pointer]
        maxProfit = 0
        left = 0  # Buying price
        right = 1  # Selling price

        while right < len(prices):

            # If we are not making any profit
            # Here right is smaller than left means we have found another minimal buying price,
            # that is at [right] so we make left = right
            if prices[left] >= prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            right += 1
        return maxProfit

# Time complexity --> O(N)
# Space complexity --> O(1)