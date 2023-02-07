# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = []

        def iterator(root, string):
            if not root:
                return

            string.append(str(root.val))

            if not root.left and not root.right:
                return

            string.append("(")
            iterator(root.left, string)
            string.append(")")

            if root.right:
                string.append("(")
                iterator(root.right, string)
                string.append(")")

        iterator(root, string)

        return ''.join(string)



