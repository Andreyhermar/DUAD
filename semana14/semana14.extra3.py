class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head

        while current is not None:
            if current.value == data:

                if current.prev is None and current.next is None:
                    self.head = self.tail = None

                elif current.prev is None:
                    self.head = current.next
                    self.head.prev = None

                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return
            current = current.next

    def print_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="")
            if temp.next is not None:
                print(" -> ", end="")
            temp = temp.next
        print()

    def print_backward(self):
        temp = self.tail
        while temp is not None:
            print(temp.value, end="")
            if temp.prev is not None:
                print(" -> ", end="")
            temp = temp.prev
        print()

dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")

print("Forward:")
dll.print_forward()

print("Backward:")
dll.print_backward()

dll.prepend("X")

print("\nAfter prepend:")
dll.print_forward()
dll.print_backward()

dll.delete("B")

print("\nAfter delete:")
dll.print_forward()
dll.print_backward()