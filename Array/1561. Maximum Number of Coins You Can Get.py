class Solution:
    def maxCoins(self, piles: [int]) -> int:
        # Sorting the piles list
        piles.sort()

        # Taking top two third of piles
        piles = piles[len(piles) // 3::]

        # Taking elements of piles with an increment of 2
        piles = piles[0::2]

        return sum(piles)