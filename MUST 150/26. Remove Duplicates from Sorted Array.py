class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        UniqueIdx = 1 # The very first value will be always unique

        for item in range(1,len(nums)):
            if nums[item]!= nums[item-1]: # That means we have found a new value
                # When we found a new value we insert it at UniqueIdx
                nums[UniqueIdx] = nums[item]
                UniqueIdx+=1

        return UniqueIdx


    # Time complexity: O(N)
    # Space complexity: O(1)