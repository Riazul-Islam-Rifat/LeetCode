class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            string = s[i+1:len(s)]+s[0:i+1]
            if string == goal:
                return True

        return False
