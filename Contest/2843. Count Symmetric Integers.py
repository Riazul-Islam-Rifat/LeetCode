class Solution:
    # Time complexity: O(n^2)
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        counter = 0
        for i in range(low, high + 1):
            num = str(i)
            if len(num) % 2 != 0:
                continue
            sum1 = 0
            sum2 = 0
            numList = list(map(int, num))
            left, right = 0, len(numList) - 1
            while left < right:
                sum1 += numList[left]
                sum2 += numList[right]
                left += 1
                right -= 1
            if sum1 == sum2:
                counter += 1

        return counter