import random

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def pre_order_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

    def level_order_traversal(self, node):
        if node is None:
            return

        queue = []
        queue.append(node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.data, end=" ")

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

    def search(self, node, data):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def delete(self, data):
        if self.root is not None:
            self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)

        return node

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def sub_tree_height(self, node):
        if node is None:
            return 0

        left_height = self.sub_tree_height(node.left)
        right_height = self.sub_tree_height(node.right)

        return max(left_height, right_height) + 1

        def count_occurrences(self, node, data):
        if node is None:
            return 0

        if node.data == data:
            return 1 + self.count_occurrences(node.left, data) + self.count_occurrences(node.right, data)
        elif data < node.data:
            return self.count_occurrences(node.left, data)
        else:
            return self.count_occurrences(node.right, data)

    def count_odd_even(self, node):
        if node is None:
            return (0, 0)

        left_counts = self.count_odd_even(node.left)
        right_counts = self.count_odd_even(node.right)

        odd_count = left_counts[0] + right_counts[0]
        even_count = left_counts[1] + right_counts[1]

        if node.data % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        return (odd_count, even_count)

def main():
    tree = Tree()

    # Cargar 1000 números aleatorios en el árbol
    for i in range(1000):
        tree.insert(random.randint(1, 10000))

    # Realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado
    print("Pre-Order Traversal: ", end="")
    tree.pre_order_traversal(tree.root)
    print()
    print("In-Order Traversal: ", end="")
    tree.in_order_traversal(tree.root)
    print()
    print("Post-Order Traversal: ", end="")
    tree.post_order_traversal(tree.root)
    print()
    print("Level-Order Traversal: ", end="")
    tree.level_order_traversal(tree.root)
    print()

    # Determinar si un número está cargado en el árbol o no
    search_num = random.randint(1, 10000)
    if tree.search(tree.root, search_num):
        print(f"{search_num} is in the tree.")
    else:
        print(f"{search_num} is not in the tree.")

    # Eliminar tres valores del árbol
    for i in range(3):
        delete_num = random.randint(1, 10000)
        tree.delete(delete_num)
        print(f"{delete_num} has been deleted from the tree.")

    # Determinar la altura del subárbol izquierdo y del subárbol derecho
    left_subtree_height = tree.sub_tree_height(tree.root.left)
    right_subtree_height = tree.sub_tree_height(tree.root.right)
    print(f"Height of left subtree: {left_subtree_height}")
    print(f"Height of right subtree: {right_subtree_height}")

    # Determinar la cantidad de ocurrencias de un elemento en el árbol
    occurrences_num = random.randint(1, 10000)
    num_occurrences = tree.count_occurrences(tree.root, occurrences_num)
    print(f"{occurrences_num} appears {num_occurrences} time(s) in the tree.")

    # Contar cuántos números pares e impares hay en el árbol
    odd_count, even_count = tree.count_odd_even(tree.root)
    print(f"There are {odd_count} odd numbers and {even_count} even numbers in the tree.")

if __name__ == "__main__":
    main()
