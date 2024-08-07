# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.path = 0

        def dfs(node, parent):
            if not node:
                return 0

            leftPath = dfs(node.left, node)
            # if node.left:
            #     print('This is the left path -- ', node.left.val, 'with value -- ', leftPath)

            rightPath = dfs(node.right, node)
            # if node.right:
            #     print('This is the right path -- ', node.right.val, 'with value -- ', rightPath)
            # print('This is the path before updating - ', self.path)
            self.path = max(self.path, leftPath + rightPath)
            # if node.left and node.right:
            #     print('This is the path length after traversing - ', node.left.val, ' and ' ,node.right.val ,' -- ', self.path)

            if parent and node.val == parent.val:
                # print('This is the parent - ', parent.val, '  This is the node - ', node.val)
                return max(leftPath, rightPath) + 1
            return 0  # When the parent and child don't match

        dfs(root, None)
        return self.path