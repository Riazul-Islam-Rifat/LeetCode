# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfSubtree(self, root) -> int:

        q = deque([root])
        nodes = 0

        def avg_calculation(root):
            summ = 0
            node = 0

            def cal(root):
                nonlocal summ
                nonlocal node
                summ += root.val
                node += 1
                if root.left:
                    cal(root.left)

                if root.right:
                    cal(root.right)

                return summ // node

            res = cal(root)
            return res

        while q:
            for item in range(len(q)):
                root = q.popleft()
                if root.left:
                    q.append(root.left)

                if root.right:
                    q.append(root.right)

                res = avg_calculation(root)

                if res == root.val:
                    nodes += 1

        return nodes

