class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # abclla--> ab-bc-cl-ll-la
        # ll
        # Output : 3
        for i in range(len(haystack)-len(needle)+1): # To get the last la we subtract -len(needle)+1
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    break
                if j == len(needle)-1: # When everything is same upto the last index
                    return i

        return -1


        # Time complexity: O(haystack*needle)
        # Space complexity: O(1)