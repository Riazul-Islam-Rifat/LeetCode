# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # We will solve the problem using inOrder traversal
        prev = None
        minDiff = float('inf')

        def inOrder(node):
            nonlocal prev, minDiff

            if not node:
                return

            inOrder(node.left)

            if prev:
                minDiff = min(minDiff, node.val - prev.val)
            prev = node  # Update prev
            inOrder(node.right)

        inOrder(root)

        return minDiff