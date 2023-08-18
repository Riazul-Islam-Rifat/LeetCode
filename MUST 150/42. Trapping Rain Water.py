class Solution:

    def trap(self, height: [int]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(1)
        leftIdx = 0
        rightIdx = len(height) - 1
        leftMax = height[leftIdx]
        rightMax = height[rightIdx]
        water = 0
        while leftIdx < rightIdx:
            if height[leftIdx] < height[rightIdx]:
                leftIdx += 1
                leftMax = max(leftMax, height[leftIdx])
                water += leftMax - height[leftIdx]

            else:
                rightIdx -= 1
                rightMax = max(rightMax, height[rightIdx])
                water += rightMax - height[rightIdx]

        return water