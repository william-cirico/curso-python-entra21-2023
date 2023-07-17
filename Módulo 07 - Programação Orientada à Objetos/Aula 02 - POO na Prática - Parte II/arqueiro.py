"""Implementação da classe Arqueiro."""

from personagem import Personagem

class Arqueiro(Personagem):
    """Arqueiro representa um personagem Arqueiro no jogo.

    Attributes:
        nome (str): O nome do arqueiro.
        nivel (int): O nível do arqueiro.
        vida (int): A quantidade de vida do arqueiro.
        precisao (int): A quantidade de precisão do arqueiro.
    """
    def __init__(self, nome, nivel, vida, precisao) -> None:
        """
        Inicializa um objeto Arqueiro.

        Attributes:
            nome (str): O nome do arqueiro.
            nivel (int): O nível do arqueiro.
            vida (int): A quantidade de vida do arqueiro.
            precisao (int): A quantidade de precisão do arqueiro.
        """
        super().__init__(nome, nivel, vida)
        self.precisao = precisao

    def atacar(self) -> None:
        """Realiza a ação de ataque do arqueiro."""
        super().atacar()
        print(f"{self.nome} dispara uma flecha com {self.precisao} de precisão!")
    
    def equipar_arco(self) -> None:
        """Realiza a ação de equipar o arco do arqueiro."""
        print(f"{self.nome} equipa o seu arco! O próximo ataque de {self.nome} causará dano adicional.")
    
    def usar_habilidade_especial(self) -> None:
        """Utiliza a habilidade especial do arqueiro."""
        print(f"{self.nome} utiliza a habilidade especial Head Shot! O inimigo que recebeu o ataque foi executado!")
