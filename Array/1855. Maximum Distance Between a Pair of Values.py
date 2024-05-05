class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # Here using the two pointer approach
        i = 0 # For nums1
        j = 0 # For nums2
        result = 0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]: # For a valid pair nums2[j] must be larger one
                i+=1
            else:
                result = max(result,j-i) # Update result for a valid pair
                j+=1

        return result