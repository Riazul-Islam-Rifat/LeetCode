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

    # Printing method in order

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.root,end=' ')

        if self.right:
            self.right.in_order()


root=BinaryTree(10)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(8)
root.insert(11)
root.insert(13)
root.insert(15)
root.insert(17)
root.in_order()

