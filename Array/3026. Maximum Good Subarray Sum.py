class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_left = defaultdict(lambda : inf)
        res = -inf
        currSum = 0

        for i in nums:
            prefix_left[i] = min(prefix_left[i],currSum)
            currSum +=i

            if i-k in prefix_left:
                res = max(res, currSum-prefix_left[i-k])

            if i+k in prefix_left:
                res = max(res, currSum-prefix_left[i+k])

        if res!=-inf:
            return res
        else:
            return 0