"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node'):
        result = []

        def postOrder(root):
            if not root:
                return
            for child in root.children:
                postOrder(child)
            result.append(root.val)

        postOrder(root)
        return result
