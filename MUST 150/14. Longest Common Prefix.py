class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        # Time complexity: O(n*m)
        # Space complexity: O(m)
        smallestStr = strs[0]
        # We are finding the smallest string because this will be the max prefix length
        for word in strs:
            if len(word)<len(smallestStr):
                smallestStr = word

        result = ''
        for char in range(len(smallestStr)):# Take a character
            for s in strs:
                # Then checks that character for all the strings
                if s[char]!=smallestStr[char]:
                    return result
            result+=smallestStr[char]

        return smallestStr

