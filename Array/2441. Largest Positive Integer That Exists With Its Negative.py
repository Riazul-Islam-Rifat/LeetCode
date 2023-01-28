class Solution:
    def findMaxK(self, nums: [int]) -> int:
        nums.sort(reverse=True)

        for item in nums:
            if -item in nums:
                return item

        return -1
