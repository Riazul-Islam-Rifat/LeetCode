class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # First we merge two arrays
        nums1.extend(nums2)
        # Sort the array
        nums1.sort()

        # Find the mid number
        midVal = nums1[len(nums1)//2]
        midValEven = (nums1[len(nums1)//2] + nums1[(len(nums1)//2)-1])/2

        if len(nums1)%2!=0:
            return midVal
        else:
            return midValEven