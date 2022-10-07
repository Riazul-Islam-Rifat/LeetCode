from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        # Initializing a variable "total_even"
        total_even = 0

        for item in nums:
            # Converting to string
            i = str(item)

            # Check whether length of i is even or odd
            # If even then add 1 with total_even
            if len(i) % 2 == 0:
                total_even += 1

        return total_even