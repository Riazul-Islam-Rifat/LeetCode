from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        # Initializing the count variable
        count = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):

                # Here i always smaller than j so if nums[i] is same as nums[j] then it will be a good pair and count will be plus 1 each time
                if nums[i] == nums[j]:
                    count += 1

        return count