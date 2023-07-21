"""
A estrutura de dados "grafo" é uma coleção de nós (também chamados de vértices) 
interconectados por arestas (também chamadas de arcos). Os grafos são uma 
representação poderosa e flexível para modelar relações entre objetos ou entidades. 
Eles são amplamente utilizados em várias áreas da ciência da computação e em 
diversos problemas do mundo real.

Aplicações do Grafo:
    * Redes Sociais
    * Sistemas de Recomendação
    * Roteamento de Redes
    * Algoritmos de Busca e Caminho Mínimo
    * Análise de Dependências
"""
from typing import List

class Graph:
    """Representa um grafo."""
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, vertex: List) -> None:
        """Adiciona uma vértica o grafo."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2) -> None:
        """Adiciona uma aresta ao grafo."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def show_graph(self) -> None:
        """Mostra o grafo."""
        for vertice in self.graph:
            print(vertice,  "->", self.graph[vertice])


if __name__ == "__main__":
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")

    graph.show_graph()
