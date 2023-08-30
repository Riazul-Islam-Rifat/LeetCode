class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        # Time complexity: O(n)
        # We will use two pointer sliding window approach
        left = 0
        right = 0
        runningSum = 0
        length = float('inf') #  Can use len(nums)+1 as minimal subarray length will never greater than len(nums)

        # We will iterate until we reach the last item
        # If the last item is added we will break the loop
        while right<len(nums):
            runningSum+=nums[right]
            # Now we will check whether total exceeds or equal to the target
            while runningSum >= target: # Means we have found a subarray
                # Find the length of the subarray
                runningLength = right-left+1
                length = min(length,runningLength) # We get the minimal length
                # Now we want to reduce the length by removing the left elements
                # Ex: nums=[2,3,1,2,4,5]; target=9
                # In the first cycle it will omit 2
                # And in the next cycle it will omit 3,1,2
                runningSum-=nums[left]
                left+=1
            right+=1
        return 0 if length == float('inf') else length