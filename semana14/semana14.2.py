
# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    # 1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    # 2. Debe incluir un método para hacer `print` de toda la estructura.
    # 3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def push_left(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def push_right(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def pop_left(self):
        if self.front is None:
            return None
        
        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        return value
    
    def pop_right(self):
        if self.rear is None:
            return None
        
        value = self.rear.value
        self.rear = self.rear.prev

        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

        return value

    def print_deque(self):
        temp = self.front
        while temp is not None:
            print(temp.value)
            temp = temp.next

dq = Deque()
dq.push_left(10)
dq.push_left(15)
dq.push_right(20)
dq.push_right(30)
dq.pop_right()

print("current Deque:")
dq.print_deque()