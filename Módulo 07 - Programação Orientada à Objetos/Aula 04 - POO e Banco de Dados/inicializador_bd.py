"""
Classe responsável por criar o banco de dados e as tabelas necessárias para armazenar 
os dados. É uma classe que segue o princípio de responsabilidade única ao encapsular
a lógica de inicialização do banco de dados.
"""

import sqlite3

class InicializadorBD:
    """Classe responsável por iniciar o banco de dados."""
    @staticmethod
    def criar_tabelas(db_nome: str):
        """Cria as tabelas no banco de dados.

        Args:
            db_nome (str): Nome do banco de dados.
        """

        connection = sqlite3.connect(db_nome)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_usuario TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        connection.commit()
        connection.close()