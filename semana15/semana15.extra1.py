class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self, value):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value
    
    def print_stack (self):
        top = self.top
        while top is not None:
            print(top.value)
            top = top.next

def bubble_sort_stack(stack):

    if stack.top is None:
        return

    swapped = True

    while swapped:
        swapped = False

        current = stack.top

        while current.next is not None:

            if current.value > current.next.value:

                current.value, current.next.value = (
                    current.next.value,
                    current.value
                )

                swapped = True

            current = current.next

stack = Stack()

stack.push(5)
stack.push(1)
stack.push(8)
stack.push(3)
stack.push(2)

print("Antes:")
stack.print_stack()

bubble_sort_stack(stack)

print("Después:")
stack.print_stack()