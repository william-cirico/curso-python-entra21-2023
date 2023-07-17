"""Implementação da classe Mago."""

from personagem import Personagem

class Mago(Personagem):
    """Mago representa um personagem Mago no jogo.

    Attributes:
        nome (str): O nome do mago.
        nivel (int): O nível do mago.
        vida (int): A quantidade de vida do mago.
        magia (int): A quantidade de magia do mago.
    """
    def __init__(self, nome, nivel, vida, magia) -> None:
        """
        Inicializa um objeto Mago.

        Attributes:
            nome (str): O nome do mago.
            nivel (int): O nível do mago.
            vida (int): A quantidade de vida do mago.
            magia (int): A quantidade de magia do mago.
        """
        super().__init__(nome, nivel, vida)
        self.magia = magia

    def atacar(self) -> None:
        """Realiza a ação de ataque do mago."""
        super().atacar()
        print(f"{self.nome} lança um feitiço poderoso com {self.magia} de magia!")
    
    def equipar_cajado(self) -> None:
        """Realiza a ação de equipar o cajado do mago."""
        print(f"{self.nome} equipa o seu cajado! O próximo ataque causará dano em área.")

    def usar_habilidade_especial(self) -> None:
        """Utiliza a habilidade especial do Mago."""
        print(f"{self.nome} utiliza a habilidade especial Meteoro! Todos os inimigos perdem 90% da vida.")