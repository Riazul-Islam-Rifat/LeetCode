class Solution:
    def targetIndices(self, nums: [int], target: int) -> [int]:

        nums.sort()

        if target in nums:
            target_index = nums.index(target)
        else:
            return []

        target_count = nums.count(target)

        output = []
        count = 0

        for item in nums:
            if item == target:
                output.append(target_index + count)
                count += 1

        return output