"""
Uma Trie (também conhecida como árvore digital, árvore de prefixos ou trie radix) é 
uma estrutura de dados especializada usada para armazenar e pesquisar um conjunto 
dinâmico de strings ou chaves associadas a valores. A palavra "Trie" vem da palavra 
"retrieval", que destaca a principal finalidade dessa estrutura: realizar operações 
eficientes de busca, inserção e exclusão em um conjunto grande de palavras ou 
strings.
"""

class TrieNode:
    """Representa um Node na Trie."""
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Representa uma Trie."""
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insere uma palavra na Trie."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Busca um elemento na Trie."""
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word
    
if __name__ == '__main__':
    trie = Trie()
    words = ["casa", "casaco", "castelo", "carro", "banana"]

    for w in words:
        trie.insert(w)

    
    print(trie.search("casa"))
    print(trie.search("cast"))
    print(trie.search("carr"))