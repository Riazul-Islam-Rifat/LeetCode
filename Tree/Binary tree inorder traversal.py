# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):

        output = []

        def inorder(root):
            nonlocal output
            if not root:
                return []

            if root.left:
                inorder(root.left)

            output.append(root.val)

            if root.right:
                inorder(root.right)

        inorder(root)
        return output