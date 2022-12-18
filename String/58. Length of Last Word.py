class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        words = s.split(' ')
        print(words)
        return len(words[-1])