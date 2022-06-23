# Creating a binary tree
class BinaryTree:
    def __init__(self,value):
        self.root=value
        self.left=None
        self.right=None

    def insert(self,val):
        if self.root:
            if val<self.root:
                if self.left is None:
                    self.left=BinaryTree(val)
                else:
                    self.left.insert(val)
            elif val>self.root:
                if self.right is None:
                    self.right=BinaryTree(val)
                else:
                    self.right.insert(val)
        else:
            self.root=val

    def summation(self,low,high):
        global summ
        if self.left:
            self.left.summation(low,high)
        if low<=self.root<=high:
            summ=summ+self.root

        if self.right:
            self.right.summation(low,high)
        return summ

node_list=[10,5,15,3,7,18]
root=BinaryTree(node_list[0])
for item in range(1,len(node_list)):
    root.insert(node_list[item])
summ=0
result=root.summation(7,15)
print(result)



### Leetcode solution ###

'''class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ=0
        def summation(root,low,high):
            nonlocal summ
            if root is None:
                return 0
            if root.left:
                summation(root.left,low,high)
            if low<=root.val<=high:
                summ=summ+root.val

            if root.right:
                summation(root.right,low,high)
        summation(root,low,high)
        return summ'''