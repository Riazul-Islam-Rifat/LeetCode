class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        tracker = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                tracker += 1
        res = tracker
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                tracker -= 1
            if s[i] in vowels:
                tracker += 1

            res = max(res, tracker)

        return res