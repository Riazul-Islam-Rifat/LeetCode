class Solution:
    def canJump(self, nums: [int]) -> bool:
        # Here we are following the greedy approach
        # Define the goal
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:  # Means we can reach the goal
                goal = i

        return goal == 0