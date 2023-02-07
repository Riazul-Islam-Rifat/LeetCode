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

    # For finding paths
    def pathPrint(self):
        path=''
        path_list=[]
        def all_path(root,path):
            if root is None:
                return ()

            if root.left is None and root.right is None:
                path = path + str(root.root) # Here first root is the object and 2nd root is the object's value
                print()
                print("After traversing a full path-- ",path)
                path_list.append(int(path))
                print("Path List", path_list)

            all_path(root.left, path + str(root.root)) # Here first root is the object and 2nd root is the object's value
            all_path(root.right, path + str(root.root)) # Here first root is the object and 2nd root is the object's value


        all_path(self,path)
        return sum(path_list)
        #return all_path(root, path)


root=BinaryTree("6")
root.insert("8")
root.insert("7")
root.insert("9")
root.insert("3")
root.insert("2")
root.insert("4")

# In order print
root.in_order()

# For path
result = root.pathPrint()
print('sum_of_all_path', result)

