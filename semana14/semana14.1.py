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


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.pop(3)
stack.print_stack()