from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time and space complexity O(n)
        num = set(nums)
        longest = 0

        for i in nums:
            # Check whether i is the first number of the sequence or not
            if i - 1 not in num:  # Means i is the first number of the sequence
                # Now check for the consecutive numbers
                total = 0
                while i + total in num:
                    total += 1  # Count total consecutive numbers

                longest = max(total, longest)

        return longest