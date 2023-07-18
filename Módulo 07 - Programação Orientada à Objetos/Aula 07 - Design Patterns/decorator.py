"""
Decorator - Padrão Estrutural

Permite adicionar novas funcionalidades a um objeto existente de forma dinâmica,
sem alterar sua estrutura básica.

O padrão Decorator é útil quando você deseja adicionar funcionalidades extras a um 
objeto de maneira flexível, em tempo de execução, e quando a herança não é uma 
opção viável. Ele permite que você envolva o objeto original com um ou vários 
decoradores, adicionando comportamentos extras sem modificar a classe original.
"""
from abc import ABC, abstractmethod

class IFonteDados(ABC):
    """Interface para a fonte de dados."""

    @abstractmethod
    def ler_dados(self) -> str:
        """Lê os dados de um input."""

class FonteDadosInput(IFonteDados):
    """Implementação concreta da fonte de dados."""
    def ler_dados(self) -> str:
        return input("Digite uma frase: ")

class FonteDadosDecorator(IFonteDados):
    """Decorador base"""
    def __init__(self, fonte_dados: IFonteDados) -> None:
        self.fonte_dados = fonte_dados

    def ler_dados(self) -> str:
        return self.fonte_dados.ler_dados()

class CriptografiaDecorator(FonteDadosDecorator):
    """Decorador de criptografia."""
    def ler_dados(self) -> str:
        """Descriptografa uma string seguindo os seguintes critérios:
        
        0 -> O
        1 -> i
        3 -> e
        4 -> a
        5 -> s

        Returns:
            A mensagem descriptografada.
        """
        CRIPTOGRAFIA = {
            "0": "o",
            "1": "i",
            "3": "e",
            "4": "a",
            "5": "s"
        }
        
        dados = super().ler_dados()
        
        mensagem_descriptografada = ""
        for caractere in dados:
            if caractere in CRIPTOGRAFIA:
                mensagem_descriptografada += CRIPTOGRAFIA[caractere]
            else:
                mensagem_descriptografada += caractere
        
        return mensagem_descriptografada
    

class CompressaoDecorator(FonteDadosDecorator):
    """Decorator de compressão."""
    def ler_dados(self) -> str:
        """Descomprime uma string ao transformar os . em espaços.
        
        Returns:
            A mensagem descomprimida.
        """
        dados = super().ler_dados()
        mensagem_descomprimida = dados.replace(".", " ")
        return mensagem_descomprimida
    

if __name__ == "__main__":
    leitor_dados = CompressaoDecorator(CriptografiaDecorator(FonteDadosInput()))
    mensagem = leitor_dados.ler_dados()
    print(mensagem)



