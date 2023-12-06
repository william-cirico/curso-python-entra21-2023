"""Implementação da classe Guerreiro."""

from personagem import Personagem

class Guerreiro(Personagem):
    """Guerreiro representa um personagem Guerreiro no jogo.

    Attributes:
        nome (str): O nome do guerreiro.
        nivel (int): O nível do guerreiro.
        vida (int): A quantidade de vida do guerreiro.
        forca (int): A quantidade de força do guerreiro.
    """
    def __init__(self, nome, nivel, vida, forca) -> None:
        """
        Inicializa um objeto Guerreiro.

        Attributes:
            nome (str): O nome do guerreiro.
            nivel (int): O nível do guerreiro.
            vida (int): A quantidade de vida do guerreiro.
            forca (int): A quantidade de força do guerreiro.
        """
        super().__init__(nome, nivel, vida)
        self.forca = forca

    def atacar(self) -> None:
        """Realiza a ação de ataque do guerreiro."""
        super().atacar()
        print(f"{self.nome} desfere um golpe com {self.forca} de força!")
    
    def equipar_escudo(self) -> None:
        """Realiza a ação de equipar o escudo do guerreiro."""
        print(f"{self.nome} equipa o seu escudo! A vida de {self.nome} aumentou.")

    def usar_habilidade_especial(self) -> None:
        """Utiliza a habilidade especial do guerreiro."""
        print(f"{self.nome} utiliza a habilidade especial Barreira de Terra! O dano do próximo ataque causado a ele ou seus aliados será mitigado.")
