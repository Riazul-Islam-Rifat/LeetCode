import math
# Time complexity: O(n^2)
class Solution:
    def minimumOperations(self, num: str) -> int:
        if int(num)%25==0:
            return 0
        lastTwoDigit = ['25','50','75','00']

        ans = float('inf')

        i = 0
        # len(num)-i-2 always gives the minimum amount of character that we need to remove from num
        while i < len(num):
            for j in range(i+1,len(num)):
                twoDigit = str(int(num[i])*10+int(num[j]))
                if twoDigit == '0':
                    twoDigit='00'
                if twoDigit in lastTwoDigit:
                    ans = min(ans,len(num)-i-2)

            i+=1

        if ans == math.inf:
            if '0' in num:
                return len(num)-1
            else:
                return len(num)
        else:
            return ans