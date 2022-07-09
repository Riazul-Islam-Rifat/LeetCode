class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:

        def max_sum(arr):
            current_sum = 0
            max_sum = 0
            for item in arr:
                current_sum = max(current_sum + item, item)
                max_sum = max(current_sum, max_sum)
            return max_sum

        if k == 1:
            return max_sum(arr)

        return ((k - 2) * max(0, sum(arr)) + max_sum(arr + arr)) % (pow(10, 9) + 7)