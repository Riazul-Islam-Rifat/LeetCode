class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        leftIdx, rightIdx = 0, 0

        while rightIdx < len(nums):
            count = 1  # As there will be at least one integer

            while rightIdx + 1 < len(nums) and nums[rightIdx] == nums[rightIdx + 1]:
                count += 1
                rightIdx += 1

            for i in range(min(2, count)):
                nums[leftIdx] = nums[rightIdx]
                leftIdx += 1

            # To continue from next unique integer
            rightIdx += 1

        return leftIdx

    # Time complexity: O(N)
    # Space complexity: O(1)