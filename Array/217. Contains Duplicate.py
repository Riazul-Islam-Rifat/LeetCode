class Solution:
    def containsDuplicate(self, nums: [int]):
        return len(nums) != len(set(nums))