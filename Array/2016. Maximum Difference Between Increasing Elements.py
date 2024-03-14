class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDif = float('-inf')
        minNum = nums[0]
        for i in range(1,len(nums)):
            maxDif = max(maxDif,nums[i]-minNum)
            minNum = min(minNum,nums[i])

        if maxDif>0:
            return maxDif
        else:
            return -1