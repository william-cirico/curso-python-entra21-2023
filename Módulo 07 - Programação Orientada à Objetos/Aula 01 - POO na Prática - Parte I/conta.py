"""Implementação da classe Conta"""
# É necessário para fazer a tipagem de uma classe em um método da própria classe
from __future__ import annotations

class Conta:
    """Conta representa uma conta bancária.
    
    Attributes:
        numero (str): Número identificador da conta.
        titular (str): Nome do títular da conta.
        saldo (float): Saldo da conta.
        limite (float): Limite da conta.
    """
    __quantidade_contas = 0 # Atributo estático

    def __init__(self, numero: str, titular: str) -> None:
        """
        Inicializa uma conta.

        Args:
            numero (str): Número da conta.
            titular (str): Títular da conta.
        
        Raises:
            AttributeError: Se `número` não possuir 9 dígitos.
        """
        if len(numero) != 9:
            raise AttributeError("número da conta deve possuir 9 dígitos")
        
        self.__numero = f"{numero[:9]}-{numero[8]}"

        # Encapsulamento
        self.__titular = titular
        self.__limite = 100
        self.__saldo = 0

        Conta.__quantidade_contas += 1
        
    @property
    def saldo(self) -> float: # Getter
        """str: Número da conta."""
        return self.__numero

    @property
    def saldo(self) -> float: # Getter
        """float: Saldo da conta."""
        return self.__saldo
    
    @property
    def limite(self) -> float: # Getter
        """float: Limite da conta."""
        return self.__limite

    @property
    def titular(self) -> str: # Getter
        """str: Nome do titular da conta."""
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: str) -> None: # Setter
        self.__titular = novo_titular.title()

    @classmethod
    def quantidade_contas(cls) -> int:
        """Retorna a quantidade de contas criadas através da classe."""
        return cls.__quantidade_contas
    
    @staticmethod
    def numero_conta_valido(numero: int) -> bool:
        """Verifica se o número da conta é valido"""
        return not isinstance(numero, int) or numero != 9

    def depositar(self, valor: float) -> None:
        """Deposita um valor no saldo da conta.
        
        Args:
            valor (float): Valor do depósito.
        """
        self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta se o saldo + limite for maior ou igual ao valor de saque.
        
        Args:
            valor (float): Valor do saque.

        Returns:
            True se for bem-sucedido, False caso contrário.
        """
        if (self.__saldo + self.__limite) < valor:
            print("Saldo indisponível para realizar a operação!")
            return False

        if self.__saldo < valor:
            self.__limite -= valor - self.saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor

        return True

    def transferir(self, valor: float, conta_destino: Conta) -> None:
        """Transfere o valor de uma conta para outra se o (saldo + limite) 
        for maior ou igual ao valor de saque.

        Args:
            valor (float): Valor da trasferência.
            conta_destino (Conta): Conta de destino da trasferência.
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Trasferência realizada com sucesso!")

    def exibir_extrato(self) -> None:
        """Exibe o extrato da conta na tela."""
        print(f"Número da conta: {self.numero}.\nSaldo: {self.saldo:.2f}.\nLimite: {self.__limite:.2f}")


if __name__ == "__main__":
    conta = Conta("123456789", "William")
    conta.depositar(20)
    conta.exibir_extrato()
    print(f"Quantidade de contas criadas: {Conta.quantidade_contas()}")

    NUMERO_CONTA = "12345678"
    if Conta.numero_conta_valido(NUMERO_CONTA):
        print(f"O número {NUMERO_CONTA} é válido")
    else:
        print(f"O número {NUMERO_CONTA} é inválido")
