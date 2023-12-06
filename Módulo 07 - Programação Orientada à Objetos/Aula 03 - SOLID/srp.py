"""
S - Single Responsibility Principle

O Princípio da Responsabilidade Única estabelece que uma classe deve ter apenas uma 
única responsabilidade, ou seja, ela deve ter apenas um motivo para ser modificada.
"""

class GerenciadorArquivo:
    """GerenciadorArquivo representa uma classe responsável por 
    lidar com operações de leitura e gravação de arquivos.
    """
    
    def ler_arquivo(self, nome_arquivo):
        """Implementa a lógica necessária para ler um arquivo."""
    
    # Violação do SRP
    def analisar_dados(self, dados):
        """Implementa a lógica necessária para analisar os dados de um arquivo."""


# O correto é criar uma classe separada
class AnaliseDados:
    """AnaliseDados representa uma classe responsável por analisar dados."""
    def analisar_dados(self, dados):
        """Implementa a lógica necessária para analisar os dados de um arquivo."""
