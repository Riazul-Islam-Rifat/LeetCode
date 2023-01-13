class Solution:
    def maxIceCream(self, costs: [int], coins: int) -> int:
        costs.sort()

        coin_used = 0
        counter = 0

        for item in costs:
            coin_used += item  # Count cost for ice cream
            if coin_used > coins:  # If cost exceeds coins then return counter
                return counter
            counter += 1

        return counter
