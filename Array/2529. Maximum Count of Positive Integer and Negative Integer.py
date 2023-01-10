class Solution:
    def maximumCount(self, nums: [int]) -> int:
        negative_num = 0
        positive_num = 0

        for item in nums:
            if item > 0:
                positive_num += 1

            elif item < 0:
                negative_num += 1

            else:
                continue

        return max(negative_num, positive_num)