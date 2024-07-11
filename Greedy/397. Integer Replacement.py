class Solution:
    def integerReplacement(self, n: int) -> int:
        min_operations = 0

        while (n!= 1):
            if n%2 ==0:
                n = int(n/2)
            else:
                if n - 1 == 2:
                    n -=1
                elif int((n + 1) / 2) %2 == 0:
                    n += 1
                else:
                    n -=1
            min_operations += 1

        return min_operations