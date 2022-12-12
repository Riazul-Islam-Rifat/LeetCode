from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for item in nums:
            tracker=[]
            for i in output:
                tracker.append(i+[item])
            output+=tracker

        return output

    # For clarification, go through the problem solutions.