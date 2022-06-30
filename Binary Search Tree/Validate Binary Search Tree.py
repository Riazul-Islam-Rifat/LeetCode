# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        tracker = []

        def in_order(root):
            nonlocal tracker
            if root.left:
                in_order(root.left)
            tracker.append(root.val)
            if root.right:
                in_order(root.right)

        in_order(root)
        flag = True
        for item in range(len(tracker) - 1):
            if tracker[item] < tracker[item + 1]:
                continue
            else:
                flag = False
        return flag
