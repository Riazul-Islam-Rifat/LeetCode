class BinaryTree:
    def __init__(self,value):
        self.root=value
        self.left=None
        self.right=None

    def insert(self,value):
        if self.root:
            if value>self.root:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right=BinaryTree(value)
            else:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left=BinaryTree(value)
        else:
            self.root=value


    def maxDepth(self):

        if not self:
            return 0
        if self.left and self.right:
            return max(self.left.maxDepth(),self.right.maxDepth())+1
        # if self.left:
        #     left = self.left.maxDepth()
        #
        # if self.right:
        #     right = self.right.maxDepth()
        # return max(left,right) + 1

root=BinaryTree("6")
root.insert("8")
root.insert("7")
root.insert("9")
root.insert("3")

result= root.maxDepth()

print(result)