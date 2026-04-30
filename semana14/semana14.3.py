# 3. Cree una estructura de objetos que asemeje un Binary Tree.
    # 1. Debe incluir un método para hacer `print` de toda la estructura.
    # 2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def print_tree(self):
        self._print_recursive(self.root)

    def _print_recursive(self, node):
        if node is None:
            return
        
        self._print_recursive(node.left)
        print(node.value)
        self._print_recursive(node.right)

tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

print("Binary Tree (in-order):")
tree.print_tree()