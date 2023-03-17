class Solution:
    def maxProductDifference(self, nums: [int]) -> int:
        nums.sort()
        return abs((nums[0]*nums[1])-(nums[-1]*nums[-2]))