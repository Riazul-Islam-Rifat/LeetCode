# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root) -> int:
        summ = 0

        def summation(root):
            nonlocal summ
            if root.left:
                if root.left.left:
                    summ += root.left.left.val

                if root.left.right:
                    summ += root.left.right.val
                    # print("left_values--", root.left.left.val)

            if root.right:
                if root.right.right:
                    summ += root.right.right.val

                if root.right.left:
                    summ += root.right.left.val
                    # print("right_values--", root.right.right.val)

        def traverse(root):
            if not root:
                return
            if root.val % 2 == 0:
                # print(root.val)
                summation(root)

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        # print(summ)
        return summ