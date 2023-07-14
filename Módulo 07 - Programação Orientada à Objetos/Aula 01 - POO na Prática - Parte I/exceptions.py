"""
Existem dois tipos de erros em Python:
    * Erros de sintaxe: Erros na forma que o código foi escrito.
      Exemplo: Escrever prnt() em vez de print().
    * Exceções: Erros detectados durante a execução que podem ser tratadas
      para que o programa não seja encerrado.

Em Python, todas as exceções são derivadas da classe BaseException e já existem
exceções padrão com por exemplo: AttributeError, TypeError, NotImplementedError.

Informações sobre as exceções padrão implementadas pelo Python:
https://docs.python.org/pt-br/3/library/exceptions.html#concrete-exceptions
"""
# Tratamento de exceções
while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
        print("Ooops! O número digitado não é um inteiro.")

# Exceção customizada
class InvalidAgeError(Exception):
    """Erro lançado quando o valor do input é menor que 18 anos."""

try:
    idade = int(input("Digite um número: "))
    
    if idade < 18:
        raise InvalidAgeError
    else:
        print("Pode votar!")
except InvalidAgeError:
    print("Exceção desparada: Idade inválida!")
