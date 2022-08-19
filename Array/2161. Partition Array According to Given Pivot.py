class Solution:
    def pivotArray(self, nums, pivot: int):
        left_arr = []
        right_arr = []
        same_arr = []
        for item in nums:
            if item < pivot:
                left_arr.append(item)
            elif item > pivot:
                right_arr.append(item)

            else:
                same_arr.append(item)

        return left_arr + same_arr + right_arr