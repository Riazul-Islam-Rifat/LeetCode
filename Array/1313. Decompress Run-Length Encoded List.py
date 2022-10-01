from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        output = []

        for item in range(0, len(nums), 2):
            freq = nums[item]
            val = nums[item + 1]

            for i in range(freq):
                output.append(val)

        return output