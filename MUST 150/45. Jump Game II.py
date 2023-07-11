class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy solution
        jumps = 0
        left = right = 0

        while right < len(nums) - 1:
            farthest = 0

            # Find the farthest
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest

            jumps += 1

        return jumps

# Time complexity: O(n)
# Space complexity: O(1)