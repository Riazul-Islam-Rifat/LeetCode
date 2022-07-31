"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import  deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        # Finding depth using level order traversal
        if not root:
            return 0

        q = deque([root])
        level = 0
        while q:
            level += 1
            size = len(q)

            for item in range(size):
                node = q.popleft()
                if node.children:
                    for child in node.children:
                        q.append(child)
        return level

