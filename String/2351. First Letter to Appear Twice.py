class Solution:
    def repeatedCharacter(self, s: str) -> str:
        tracker = {}
        for item in s:
            if item in tracker:
                return item
            else:
                tracker[item]=True

        return