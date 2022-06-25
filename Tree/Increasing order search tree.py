# Leetcode solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        final_tree = expected_tree = TreeNode()

        # print(id(final_tree))
        # print(id(expected_tree))
        def new_tree(root):
            nonlocal expected_tree
            if root:
                new_tree(root.left)
                expected_tree.right = TreeNode(root.val)
                expected_tree = expected_tree.right
                new_tree(root.right)
            # print("----",id(expected_tree))

        new_tree(root)
        return final_tree.right    
