class Solution:
    def differenceOfSum(self, nums: [int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for item in nums:
            if item < 10:
                digit_sum += item

            elif item == 10:
                digit_sum += 1
            else:
                while item > 0:
                    remainder = item % 10
                    digit_sum += remainder
                    item = item // 10

        return abs(digit_sum - element_sum)
