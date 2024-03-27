class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def DaoNguoc(self):
        if self.head is None:
            return

        stack = []
        current = self.head

        while current is not None:
            stack.append(current)
            current = current.next

        self.head = stack.pop()
        current = self.head

        while stack:
            node = stack.pop()
            current.next = node
            current = current.next

        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.info, end=" ")
            current = current.next
        print()

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

print("Danh sách liên kết ban đầu:")
llist.display()

llist.DaoNguoc()

print("Danh sách liên kết sau khi đảo ngược:")
llist.display()
