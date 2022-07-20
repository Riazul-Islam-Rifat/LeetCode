"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node'):
        result = []

        def preOrder(root):
            nonlocal result
            if not root:
                return

            result.append(root.val)

            for child in root.children:
                preOrder(child)

        preOrder(root)
        return result


