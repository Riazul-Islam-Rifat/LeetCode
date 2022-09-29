class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:

        # Initializing the output list
        output = []

        for item in candies:
            if (item + extraCandies) >= max(candies):
                output.append(True)

            else:
                output.append(False)

        return output