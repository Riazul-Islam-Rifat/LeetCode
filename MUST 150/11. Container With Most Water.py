class Solution:
    def maxArea(self, height: [int]) -> int:
        # Time complexity: O(N)
        # Space complexity: O(1)
        water = 0
        left = 0
        right = len(height)-1

        while left<right:
            # Find the current amount of water
            width = right-left
            min_height = min(height[left],height[right]) # We take the min height of left and right.
            current_water = min_height * width
            water = max(water,current_water)

            if height[left]<height[right]: # We want max height and width to get the maximum water
                left+=1
            elif height[left]>height[right]:# We want max height and width to get the maximum water
                right-=1
            else:
                left+=1 # We can also shift the right pointer
        return water