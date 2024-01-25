class Solution:
    def numberGame(self, nums: [int]) -> [int]:
        arr = []
        while len(nums)>=2:
            min1 = min(nums)
            nums.remove(min1)
            min2 = min(nums)
            nums.remove(min2)

            arr.append(min2)
            arr.append(min1)

        return arr