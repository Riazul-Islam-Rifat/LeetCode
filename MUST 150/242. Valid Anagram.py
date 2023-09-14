from collections import Counter
class Solution:
    # Time and space complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        S = dict(Counter(s))
        T = dict(Counter(t))

        return S==T