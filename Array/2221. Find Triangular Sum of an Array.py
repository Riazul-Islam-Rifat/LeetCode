class Solution:
    def triangularSum(self, nums: [int]) -> int:

        if len(nums) == 1:
            return nums[0]

        while len(nums) > 1:

            tracker = []

            for item in range(len(nums) - 1):
                tracker.append((nums[item] + nums[item + 1]) % 10)

            nums = tracker

        return tracker[0]
