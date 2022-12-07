from collections import defaultdict
from typing import List
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        tracker = defaultdict(int)
        counter = 0
        for num in nums:
            tmp1, tmp2 = num - k, num + k
            if tmp1 in tracker:
                counter += tracker[tmp1]
            if tmp2 in tracker:
                counter += tracker[tmp2]

            tracker[num] += 1

        return counter