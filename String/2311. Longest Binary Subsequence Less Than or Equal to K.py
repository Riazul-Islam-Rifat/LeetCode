class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Trace this code with 3/4 examples to understand how does it work -_-
        start = ""
        res = 0
        for digit in reversed(s):
            start = digit + start
            if int(start, 2) <= k:
                res += 1
            elif digit == '0':
                res += 1

        return res