from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        output = []

        for item in nums:
            if item % 2 == 0:
                output.insert(0, item)

            else:
                output.append(item)

        return output