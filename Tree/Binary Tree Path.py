# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        output = []
        path = ''

        def path_finding(root, path):
            if not root:
                return []

            if root.left is None and root.right is None:
                path += str(root.val)
                output.append(path)

            path_finding(root.left, path + str(root.val) + "->")
            path_finding(root.right, path + str(root.val) + "->")

        path_finding(root, path)
        return output