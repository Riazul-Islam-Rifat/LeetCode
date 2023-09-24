class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        # Time and space complexity- O(n)
        # We need to find whether there is duplicate or not in the array window  of length 0 to k
        kWindow = set()  # Store the unique numbers
        left = 0

        for right in range(len(nums)):
            if right - left > k:  # Means we have exceeded the k window
                kWindow.remove(nums[left])  # Remove the left most item
                left += 1

            if nums[right] in kWindow:  # If we encounter a value for the 2nd time  we return True
                return True

            kWindow.add(nums[right])  # Everytime we add an item to the set

        return False




