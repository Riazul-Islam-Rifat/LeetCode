class GenericTree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def addChild(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        parent=self.parent
        while parent:
            level+=1
            parent=parent.parent
        return level

    def printTree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix,self.data)
        for child in self.children:
            child.printTree()

# In N-ary tree every child will be passed as an object of the tree class
root=GenericTree(1)

branch1=GenericTree(2)
branch1.addChild(GenericTree(3))
branch1.addChild(GenericTree(4))

branch2=GenericTree(5)
branch2.addChild(GenericTree(6))

root.addChild(branch1)
root.addChild((branch2))

root.printTree()
#print("Level of branch1 --> ", branch1.get_level())
