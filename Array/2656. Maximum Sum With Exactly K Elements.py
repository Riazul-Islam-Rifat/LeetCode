class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0

        for i in range(k):
            maximum = max(nums)
            nums.remove(maximum)
            nums.append(maximum + 1)
            score += maximum

        return score
