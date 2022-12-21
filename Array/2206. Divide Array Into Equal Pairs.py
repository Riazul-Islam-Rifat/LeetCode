from typing import List
from collections import defaultdict
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        tracker = defaultdict(int)

        for item in nums:
                tracker[item]+=1

        for item in tracker.keys():
            if tracker[item]%2!=0:
                return False

        return True