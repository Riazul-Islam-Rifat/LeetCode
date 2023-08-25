class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Time complexity O(n)
        tracker = 0
        # We need to find the strings of s in the same sequence in string t
        for char in t:
            if tracker == len(s):  # Means we have found all the characters of s in the given sequence in t
                break
            if char == s[tracker]:
                tracker += 1

        return tracker == len(s)