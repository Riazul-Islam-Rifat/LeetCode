class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        # initializing some variables
        idx1 = m-1 # Index tracker for the nums1 array
        idx2 = n-1 # Index tracker for the nums2 array
        idx = m+n-1 # Index tracker for the output array [nums1]

        # When there will be availabe index/values in nums2 array we will keep comparing
        while idx2 >=0:

            if idx1>=0 and nums1[idx1]>nums2[idx2]:# idx1>=0 This check for the leftover values in nums2 array
                nums1[idx] = nums1[idx1]
                idx1-=1
            else:
                nums1[idx]=nums2[idx2]
                idx2-=1
            idx-=1
        return nums1


    ###################################################################

    # Time complexity- O(n)
    # Space complexity- O(1) As we are not using any additional data structure