# # creating a node
class Node:
    def __init__(self, value):
        self.data= value
        self.next = None

# # creating the head
class LinkedListHead:
    def __init__(self):
        self.head = None

    def insert(self, value):

        newNode= Node(value)

        if self.head:
            current = self.head
            while (current.next):
                current = current.next
            current.next= newNode

        else:
            self.head = newNode

    def print_LinkedList(self):
        current= self.head
        while current:
            print('--> ', current.data, end=' ')
            current = current.next

linkedList = LinkedListHead()

linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(3)
linkedList.insert(4)
linkedList.insert(5)

print("Printing the linked list ")

linkedList.print_LinkedList()



