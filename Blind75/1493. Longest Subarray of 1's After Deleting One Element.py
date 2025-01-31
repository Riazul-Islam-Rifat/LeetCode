class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        k = 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                k += 1
            while k > 1:

                if nums[l] == 0:
                    k -= 1
                l += 1
            res = max(r - l, res)
            r += 1

        return res - 1 if res == len(nums) else res