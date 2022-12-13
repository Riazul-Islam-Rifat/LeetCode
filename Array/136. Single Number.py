class Solution:
    def singleNumber(self, nums: [int]) -> int:
        for item in nums:
            if nums.count(item)==1:
                return item