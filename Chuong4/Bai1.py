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

    def InNguocRecursive(self, node):
        if node is None:
            return
        self.InNguocRecursive(node.next)
        print(node.info, end=" ")

    def InNguocIterative(self):
        if self.head is None:
            return

        stack = []
        current = self.head

        while current is not None:
            stack.append(current)
            current = current.next

        while stack:
            node = stack.pop()
            print(node.info, end=" ")

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

print("In ngược danh sách bằng phương thức đệ qui:")
llist.InNguocRecursive(llist.head)
print("\nIn ngược danh sách bằng phương thức không đệ qui:")
llist.InNguocIterative()
