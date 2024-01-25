class Solution:
    def separateDigits(self, nums: [int]) -> [int]:
        output = []

        for item in nums:
            num = str(item)
            for i in num:
                output.append(int(i))

        return output