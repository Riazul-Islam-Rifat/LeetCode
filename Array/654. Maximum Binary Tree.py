# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums) -> [TreeNode]:
        if not nums:
            return None
        max_val=max(nums)
        index=nums.index(max_val)
        root = TreeNode(max_val)
        root.left=self.constructMaximumBinaryTree(nums[0:index]) # Take the left subarray
        root.right=self.constructMaximumBinaryTree(nums[index+1:]) # Take the right subarray
        return root