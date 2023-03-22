class Solution:
    def minOperations(self, nums: [int]) -> int:
        minimumOperation = 0
        for item in range(len(nums)-1):
            if nums[item]<nums[item+1]:
                continue
            else:
                prevValue = nums[item+1]
                nums[item+1]=nums[item]+1
                minimumOperation+= nums[item+1]-prevValue
        return minimumOperation