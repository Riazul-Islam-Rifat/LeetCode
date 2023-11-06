class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This code runs in  O(n^2) time
        # maxSum = 0
        # for i in range(len(nums)):
        #     maxSum = max(maxSum,nums[i])
        #     for j in range(i+1,len(nums)):
        #         subArr  = nums[i:j+1]
        #         maxSum = max(maxSum,sum(subArr))
        # return maxSum

        # This code runs in  O(n) time
        maxSum = nums[0]  # Initial max sum
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0  # We never want to add up negative value

            curSum += num

            maxSum = max(maxSum, curSum)

        return maxSum
