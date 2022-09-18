from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # Initializing output
        output = []

        for index, item in enumerate(l):
            # Initializing flag
            flag = True

            # creating sub_array of nums
            sub_array = nums[item:r[index] + 1]
            # Sorting the sub_array
            sub_array.sort()
            # Storing the difference in diff
            diff = sub_array[0] - sub_array[1]

            for item in range(1, len(sub_array) - 1):

                # Flag  will be false when difference of two consecutive values will not be as same as diff
                if sub_array[item] - sub_array[item + 1] != diff:
                    flag = False
                    break

            output.append(flag)

        return output