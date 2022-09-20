from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # Initializing output list
        output = []

        for item in nums:
            count = 0
            for i in nums:
                if i < item:
                    count += 1

            output.append(count)

        return output