class Solution:
    def getCommon(self, nums1: [int], nums2: [int]) -> int:
        i = 0 # Tracks nums1
        j = 0 # Tracks nums2

        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1

        return -1