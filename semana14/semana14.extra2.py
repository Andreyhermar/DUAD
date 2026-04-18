class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.value == data:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.value == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def print_all(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="")
            if temp.next is not None:
                print(" -> ", end="")
            temp = temp.next
        print()

ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)

print("after insert_front:")
ll.print_all()

ll.insert_back(30)

print("after insert_back:")
ll.print_all()


ll.delete(10)

print("after delete:")
ll.print_all()