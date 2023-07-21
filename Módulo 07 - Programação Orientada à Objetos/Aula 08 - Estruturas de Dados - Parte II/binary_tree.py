"""
Árvore Binária

Uma árvore binária é uma estrutura de dados não linear que organiza os elementos de forma 
hierárquica. Ela é composta por um conjunto de nós, onde um dos nós é designado 
como nó raiz e os demais são divididos em subárvores. Cada nó pode ter zero ou mais 
nós filhos, que são conectados por arestas.
"""
from typing import Any

class TreeNode:
    """Representa a estrutura de dados de Árvore."""
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    "Representa uma arvore binária."
    def __init__(self):
        self.root = None

    def insert(self, value: Any) -> None:
        """Insere um elemento na árvore binária."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value: Any, current_node: TreeNode) -> None:
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(value, current_node.right)
        else:
            # Ignore duplicate values (you can change this behavior if needed)
            pass

    def search(self, value: Any) -> TreeNode:
        """Busca um elemento na árvore binária."""
        return self._search_recursive(value, self.root) if self.root else None

    def _search_recursive(self, value: Any, current_node: TreeNode) -> TreeNode:
        if current_node is None or current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self._search_recursive(value, current_node.left)
        else:
            return self._search_recursive(value, current_node.right)

tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print(tree.search(4))
print(tree.search(9))
