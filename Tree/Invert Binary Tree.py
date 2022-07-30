# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root) :
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


#  To print level order root --> right --> left -->
#         output=[]
#         q= deque([root])
#         if not root:
#             return []
#         while q:
#             for item in range(len(q)):
#                 root=q.popleft()
#                 output.append(root.val)
#                 #expected_tree=TreeNode(root)
#                 if root.right:
#                     q.append(root.right)
#                     #expected_tree.left=TreeNode((root.right))
#                 if root.left:
#                     q.append(root.left)
#                     #expected_tree.right=TreeNode((root.left))
#         print(output)




