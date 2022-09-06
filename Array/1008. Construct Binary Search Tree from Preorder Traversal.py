# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        # Creating the main root of the tree
        root = TreeNode(preorder[0])

        # Omitting the first value which is assigned already as a root value from preorder list
        preorder = preorder[1:len(preorder)]

        # Creating insert function to insert value in BST
        def insert(root, val):
            if not root:
                return TreeNode(val)

            # Greater value than the root value is assgned in the right part of the tree
            if val > root.val:
                root.right = insert(root.right, val)

            # Smaller value than the root value is assigned in the left part of the tree
            else:
                root.left = insert(root.left, val)

            # Each time the updated root is returned
            return root

        for item in preorder:
            # In each iteration calling the insert function to insert value in BST
            root = insert(root, item)

        return root
