from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Initializing the output list
        output = []

        for item in range(len(nums)):
            # inserting nums[item] in index[item]
            output.insert(index[item], nums[item])

        return output