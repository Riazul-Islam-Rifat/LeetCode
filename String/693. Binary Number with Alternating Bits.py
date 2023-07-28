class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binNum = bin(n)[2::]
        for i in range(1,len(binNum)):
            if binNum[i]==binNum[i-1]:
                return False

        return True