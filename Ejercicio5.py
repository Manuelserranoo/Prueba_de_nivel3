import random

# Definir la clase del nodo del árbol
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

# Definir la clase del árbol
class BinaryTree:
    def __init__(self):
        self.root = None

    # Método para agregar un nodo al árbol
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    # Método para realizar el barrido preorden
    def pre_order_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # Método para realizar el barrido inorden
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.val, end=" ")
            self.in_order_traversal(node.right)

    # Método para realizar el barrido postorden
    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.val, end=" ")

    # Método para realizar el barrido por nivel
    def level_order_traversal(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            current_node = queue.pop(0)
            print(current_node.val, end=" ")
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    # Método para buscar un valor en el árbol
    def search(self, val):
        current = self.root
        while current:
            if current.val == val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

    # Método para eliminar un nodo del árbol
    def delete(self, val):
        if self.root is None:
            return self.root
        elif val < self.root.val:
            self.root.left = self.delete_node(self.root.left, val)
        elif val > self.root.val:
            self.root.right = self.delete_node(self.root.right, val)
        else:
            if self.root.left is None:
                temp = self.root.right
                self.root = None
                return temp
            elif self.root.right is None:
                temp = self.root.left
                self.root = None
                return temp
            temp = self.get_min_node(self.root.right)
            self.root.val = temp.val
            self.root.right = self.delete_node(self.root.right, temp.val)
        return self.root

    # Método auxiliar para eliminar un nodo del árbol
    def delete_node(self, node, val):
        if node is None:
            return node
        if val < node.val:
            node.left = self.delete_node(node.left, val)
        elif val > node.val:
            node.right = self.delete_node(node.right, val)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.get_min_node(node.right)
            node.val = temp.val
            node.right = self.delete_node(node.right, temp.val)
        return node

    # Método auxiliar para encontrar el nodo con el valor mínimo
    def get_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Método para encontrar la altura del subárbol izquierdo
    def left_subtree_height(self, node):
        if node is None or node.left is None and node.right is None:
            return 0
        else:
            return 1 + max(self.left_subtree_height(node.left), self.left_subtree_height(node.right))

    # Método para encontrar la altura del subárbol derecho
    def right_subtree_height(self, node):
        if node is None or node.left is None and node.right is None:
            return 0
        else:
            return 1 + max(self.right_subtree_height(node.left), self.right_subtree_height(node.right))

    # Método para contar la cantidad de ocurrencias de un elemento en el árbol
    def count_occurrences(self, val, node):
        if node is None:
            return 0
        if node.val == val:
            return 1 + self.count_occurrences(val, node.left) + self.count_occurrences(val, node.right)
        elif val < node.val:
            return self.count_occurrences(val, node.left)
        else:
            return self.count_occurrences(val, node.right)

    # Método para contar la cantidad de números pares e impares en el árbol
    def count_parity(self, node, even=0, odd=0):
        if node is None:
            return even, odd
        if node.val % 2 == 0:
            even += 1
        else:
            odd += 1
        even, odd = self.count_parity(node.left, even, odd)
        even, odd = self.count_parity(node.right, even, odd)
        return even, odd
if __name__ == "__main__":
    # Crear un árbol binario y cargar 1000 números aleatorios
    binary_tree = BinaryTree()
    for i in range(1000):
        binary_tree.insert(random.randint(0, 10000))

    # Realizar los barridos del árbol
    print("Preorden: ")
    binary_tree.pre_order_traversal(binary_tree.root)
    print("\nInorden: ")
    binary_tree.in_order_traversal(binary_tree.root)
    print("\nPostorden: ")
    binary_tree.post_order_traversal(binary_tree.root)
    print("\nPor nivel: ")
    binary_tree.level_order_traversal(binary_tree.root)

    # Buscar un número en el árbol
        # Contar la cantidad de ocurrencias de un número en el árbol
    val = 5000
    count = binary_tree.count_occurrences(val, binary_tree.root)
    print("\nEl valor {} aparece {} veces en el árbol.".format(val, count))

    # Eliminar tres valores del árbol
    binary_tree.delete(5000)
    binary_tree.delete(6000)
    binary_tree.delete(7000)

    # Encontrar la altura del subárbol izquierdo y derecho
    left_height = binary_tree.left_subtree_height(binary_tree.root)
    right_height = binary_tree.right_subtree_height(binary_tree.root)
    print("\nLa altura del subárbol izquierdo es {} y la altura del subárbol derecho es {}.".format(left_height, right_height))

    # Contar la cantidad de números pares e impares en el árbol
    even_count, odd_count = binary_tree.count_parity(binary_tree.root)
    print("\nEl árbol tiene {} números pares y {} números impares.".format(even_count, odd_count))

