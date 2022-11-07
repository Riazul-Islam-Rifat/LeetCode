class Solution:
    def kthDistinct(self, arr: [str], k: int) -> str:

        # Initializing a tracker to store distinct strings along with it's index
        tracker = {}
        # ith_str is initialized to track ith distinct string
        ith_str = 0

        for item in range(len(arr)):

            if arr.count(arr[item]) == 1:
                ith_str += 1
                tracker[ith_str] = arr[item]

        # Returning kth distinct string if it is available in tracker's keys
        if k in tracker.keys():
            return tracker[k]

        else:
            return ''

