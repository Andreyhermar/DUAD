class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def print_all(self):
        temp = self.front
        while temp is not None:
            print(temp.value, end="")
            if temp.next is not None:
                print(" -> ", end="")
            temp = temp.next
        print()

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("Queue actual:")
q.print_all()

print("\nDequeue:", q.dequeue())

print("\nQueue después de dequeue:")
q.print_all()