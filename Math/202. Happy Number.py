class Solution:
    def isHappy(self, n: int) -> bool:
        tracker = set()
        while n != 1:
            if n in tracker:  # It breaks the infinite loop. If we counter the number more than once this means we will get in again and again. So finding a number twice will result False
                return False
            tracker.add(n)
            num = str(n)
            sqrN = 0
            for i in num:
                sqrN += int(i) ** 2
            n = sqrN

        return True