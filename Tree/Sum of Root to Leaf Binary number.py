# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root):
        path = ""
        path_tracker = []

        def leaf_sum(root, path):
            if root is None:
                return

            if root.left is None and root.right is None:
                path += str(root.val)
                path_tracker.append(int(path, 2))

            leaf_sum(root.left, path + str(root.val))
            leaf_sum(root.right, path + str(root.val))

        leaf_sum(root, path)
        return (sum(path_tracker))