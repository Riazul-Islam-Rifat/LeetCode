import collections
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tracker = collections.Counter(nums)
        output=[]
        for key, value in tracker.items():
            if value>len(nums)//3:
                output.append(key)

        return output