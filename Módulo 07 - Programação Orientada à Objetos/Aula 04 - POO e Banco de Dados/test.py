"""
Para realizar a conexão com o banco de dados podemos utilizar o driver do BD ao
qual queremos realizar a conexão.

Nesse exemplo vamos utilizar o sqlite que já possui o driver integrado no python.
"""
from inicializador_bd import InicializadorBD
from usuario_repositorio import UsuarioRepositorio
from usuario import Usuario

# Inicializando BD
DB_NOME = "exemplo.db"
InicializadorBD.criar_tabelas(DB_NOME)

# Inicializando o repositório
usuario_repositorio = UsuarioRepositorio(DB_NOME)

# Criando instâncias dos usuários
usuario1 = Usuario("William", "william@email.com")
usuario2 = Usuario("Maria", "maria@email.com")

# Inserindo usuários
usuario1 = usuario_repositorio.inserir_usuario(usuario1)
usuario2 = usuario_repositorio.inserir_usuario(usuario2)

print(usuario1, usuario2)

# Atualizando usuário
usuario1.email = "email@atualizado.com"
usuario_repositorio.atualizar_usuario(usuario1)

# Removendo usuário
usuario_repositorio.remover_usuario(usuario2)

# Consultando usuários
usuarios = usuario_repositorio.obter_usuarios()
print(usuarios)
