from __future__ import annotations
from random import randint
from abc import ABC, abstractmethod

class BankAccount(ABC):
    """BankAccount representa uma conta bancária.

    Args:
        holder (str): Nome do titular da conta.
    """

    def __init__(self, holder: str):
        self.__registration = randint(1, 100_000)
        self.holder = holder
        self.__balance = 0
        
    def __str__(self):
        return f"Titular: {self.holder} | Saldo: {self.__balance}"

    @property
    def registration(self):
        """(int): Número da conta."""
        return self.__registration

    @property
    def balance(self):
        """(float): Saldo da conta."""
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Saldo não pode ser negativo.")
            self.__balance = value

    def withdraw(self, amount: float) -> bool:
        """Saca um valor da conta.

        Args:
            amount (float): Valor que será sacado.

        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        
        return False
    
    def deposit(self, amount: float):
        """Deposita um valor na conta.
        
        Args:
            amount (float): Valor que será depositado na conta.
        """
        tax = self.get_deposit_tax()
        
        self.__balance += amount * (1 - tax)
        
    def transfer(self, amount: float, target_account: BankAccount):
        """Transfere um valor para outra conta.
        
        Args: 
            amount (float): Valor que será transferido.
            target_account (BankAccount): Conta de destino da transferência.
        """
        if (self.withdraw(amount)):
            target_account.deposit(amount)
        else:
            print("Não foi possível realizar a transferência: Saldo indisponível.")
            
    @abstractmethod
    def get_deposit_tax(self) -> float:
        """Obtém a taxa de depósito da conta bancária."""
