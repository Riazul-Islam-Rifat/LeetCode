import math
class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        output=[]

        for item in nums:
            #square=int(math.pow(item,2))
            output.append(int(math.pow(item,2)))

        output.sort()

        return output