# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def deepestLeavesSum(self, root) -> int:
        q = deque([root])
        level = 0
        while q:
            level += 1
            for item in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        summation = 0
        q = deque([root])
        new_level = 0
        while q:
            new_level += 1
            for item in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                if new_level == level:
                    summation += node.val

        return summation