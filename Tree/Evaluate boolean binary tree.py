# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root):
        # Method-->1
        def traverse(root):
            if root.val == 2:
                return traverse(root.left) or traverse(root.right)
            elif root.val == 3:
                return traverse(root.left) and traverse(root.right)
            return root.val

        return traverse(root)

        # Method 2 -->
        # if root.val == 2:
        #     return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # elif root.val == 3:
        #     return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        #
        # return root.val