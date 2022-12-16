from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        tracker = set()

        for item in nums:
            if item in tracker:
                result.append(item)

            else:
                tracker.add(item)

        return result