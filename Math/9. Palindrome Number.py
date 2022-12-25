class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False

        revertNum = 0

        while x > revertNum:
            revertNum = revertNum * 10 + x % 10
            x = x // 10

        return x == revertNum or x == revertNum // 10