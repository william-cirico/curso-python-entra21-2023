"""Modelo de usuário"""

class Usuario:
    """Classe para representar um usuário.

    Attributes:
        id (int): ID do usuário.
        nome_usuario (str): Nome do usuário.
        email (str): E-mail do usuário.
    """
    def __init__(self, nome_usuario: str, email: str, id: int = None) -> None:
        """Inicializa um usuário.
        
        Args:
            id (int): ID do usuário.
            nome_usuario (str): Nome do usuário.
            email (str): E-mail do usuário.
        """
        self.id = id
        self.nome_usuario = nome_usuario
        self.email = email

    def __repr__(self) -> str:
        return f"Usuário({self.id}, '{self.nome_usuario}', '{self.email}')"
