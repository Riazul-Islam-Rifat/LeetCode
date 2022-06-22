class BinaryTree:

    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None

    # Inserting value to the left and right of the root
    def insert(self,value):
        global arr
        if self.root:
            if value<self.root:
                if self.left is None:
                    self.left=BinaryTree(value)
                    arr.append(self.left.root)
                else:
                    self.left.insert(value)

            elif value>self.root:
                if self.right is None:
                    self.right=BinaryTree(value)
                    arr.append(self.right.root)
                else:
                    self.right.insert(value)
        else:
            self.root=value
            arr.append(self.root)
    @staticmethod
    def root_sum():
        if arr[0]==arr[1]+arr[2]:
            print("True")
        else:
            print("False")
    # For leetcode submission 
    '''class Solution:
        def checkTree(self, root: Optional[TreeNode]) -> bool:
            return root.val == root.left.val + root.right.val'''

arr=[]
tree=BinaryTree(5)
arr.append(tree.root)
tree.insert(3)
tree.insert(1)
tree.root_sum()