class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        nums = set(banned)
        summ = 0
        ans = 0
        for i in range(1, n + 1):
            if i not in nums and summ + i <= maxSum:
                ans += 1
                summ += i

        return ans