from typing import  List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        if not root1 and not root2:
            return

        # Initializing the output list
        output = []

        # Writing forRoot method to traverse tree and insert it's value in the output list
        def forRoot(root):

            nonlocal output

            # Implementing in order traversing
            if root.left:
                forRoot(root.left)

            output.append(root.val)

            if root.right:
                forRoot(root.right)

        if root1:
            forRoot(root1)

        if root2:
            forRoot(root2)

        output.sort()
        return output