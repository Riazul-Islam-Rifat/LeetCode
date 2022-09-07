from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort the nums list
        nums.sort()
        # store  len of nums in length
        length = len(nums) - 1
        # Initialize pair_sum variable as 0
        pair_sum = 0

        for item in range(len(nums) // 2):
            # calculate sum of a pair and update pair_sum with max pair_sum value
            pair_sum = max(pair_sum, (nums[item] + nums[length]))
            length -= 1  # Decrease length by 1 in each iteration

        return pair_sum