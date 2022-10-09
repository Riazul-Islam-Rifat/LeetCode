from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        # Initializing a variable triplet
        triplet = 0

        for item in range(len(nums)):
            # nums[item] = nums[i], ij = nums[j]
            ij = nums[item] + diff

            # ij = nums[j],  jk = nums[k]
            jk = ij + diff

            if ij in nums and jk in nums:
                triplet += 1

        return triplet
