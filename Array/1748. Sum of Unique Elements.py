class Solution:
    def sumOfUnique(self, nums: [int]) -> int:
        sum = 0

        for item in nums:
            if nums.count(item)==1:
                sum+=item

        return sum