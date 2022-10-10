# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Initializing a list to store values of the tree
        tree_val = []

        def in_order(root):
            nonlocal tree_val

            # Traversing the left part
            if root.left:
                in_order(root.left)

            tree_val.append(root.val)

            # Traversing the right part
            if root.right:
                in_order(root.right)

        in_order(root)

        # creating a Balance Binary search tree.
        def BBST(tree_val, start, end):
            if start > end:
                return
            mid = (end - start) // 2
            root = TreeNode(tree_val[mid])  # root
            root.left = BBST(tree_val[:mid], 0, mid - 1)  # left
            root.right = BBST(tree_val[mid + 1:], mid + 1, len(tree_val) - 1)  # right
            return root

        length = len(tree_val)
        return BBST(tree_val, 0, length)