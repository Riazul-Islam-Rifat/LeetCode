# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root) -> bool:
        flag = True

        def traverse(root, target):
            nonlocal flag
            if root.val != target:
                flag = False

            if root.left:
                traverse(root.left, target)

            if root.right:
                traverse(root.right, target)

        traverse(root, root.val)
        return flag