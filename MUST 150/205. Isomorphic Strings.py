class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time and space complexity : O(N)
        S = {}
        T = {}

        for i in range(len(s)):  # Preserves the order
            c1 = s[i]
            c2 = t[i]
            # Ensuring that two characters are not mapped to a same character
            if ((c1 in S and S[c1] != c2) or (c2 in T and T[c2] != c1)):
                return False
            # Mapping characters for both strings s and t
            S[c1] = c2
            T[c2] = c1

        return True