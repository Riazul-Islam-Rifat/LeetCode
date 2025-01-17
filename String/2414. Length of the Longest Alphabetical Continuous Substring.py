class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 0
        tracker = 1
        for i in range(len(s)-1):
            if ord(s[i+1])-ord(s[i]) == 1:
                tracker+=1
            else:
                res = max(res,tracker)
                tracker = 1

        return max(res,tracker)
