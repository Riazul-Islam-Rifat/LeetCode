class Solution:
    def sortColors(self, nums: [int]) -> None:
        for item in range(1, len(nums)):
            j = item

            while j > 0 and nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1



