class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(N) space
        # strs = s.lower()
        # alphabet = set(string.ascii_lowercase)
        # number = {'1','2','3','4','5','6','7','8','9','0'}
        # sList = []
        # for char in strs:
        #     if char in alphabet or char in number:
        #         sList.append(char)

        # finalStr = ''.join(sList)

        # left = 0
        # right = len(finalStr)-1

        # while left < right:
        #     if finalStr[left]!=finalStr[right]:
        #         return False
        #     left+=1
        #     right-=1

        # return True

        # O(1) Space
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True