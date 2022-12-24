from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

    # As the majority element appears more than [n/2] times hence that element will be the [n//2]th element after sorting
        nums.sort()
        return nums[len(nums)//2]