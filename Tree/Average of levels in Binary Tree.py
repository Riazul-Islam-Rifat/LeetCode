# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root):
        q = deque([root])
        output = []
        while q:
            current_sum = 0
            total_num = 0
            for item in range(len(q)):
                root = q.popleft()
                current_sum += root.val
                total_num += 1
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            avg = current_sum / total_num
            output.append(avg)

        return output
