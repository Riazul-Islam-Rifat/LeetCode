import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        power = math.log2(abs(n))

        if power == int(power):
            return True
        else:
            return False