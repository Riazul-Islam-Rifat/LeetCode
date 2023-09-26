class Solution:
    def summaryRanges(self, nums):
        # Time complexity: O(N)
        if not nums:
            return []

        intervals = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # Means we have found a gap more than 1
                if start == nums[i - 1]:  # When there is a single number in the range
                    intervals.append(str(start))
                else:
                    intervals.append(
                        str(start) + "->" + str(nums[i - 1]))  # When there are multiple numbers in the range
                start = nums[i]  # Update the start

        # Handle the last range
        if start == nums[-1]:
            intervals.append(str(start))  # When only the last number left
        else:
            intervals.append(str(start) + "->" + str(nums[-1]))

        return intervals
