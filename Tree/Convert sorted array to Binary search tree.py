# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) :
        if not nums:
            return None

        # Creating the root
        # Here root will always be the mid value of the list

        mid_val = len(nums) // 2  # Taking the floor value

        root = TreeNode(nums[mid_val])  # Here root_val is the mid value of the list

        # Now we will create left and right object of the root

        root.left = self.sortedArrayToBST(nums[:mid_val])
        root.right = self.sortedArrayToBST(nums[mid_val + 1:])

        return root