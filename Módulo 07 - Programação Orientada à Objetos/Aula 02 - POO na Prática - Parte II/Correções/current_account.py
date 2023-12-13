from bank_account import BankAccount

class CheckingAccount(BankAccount):
    """CheckingAccount representa uma conta corrente."""
    def __init__(self, holder: str, limit: float):
        super().__init__(holder)
        self.__limit = limit
        
    @property
    def limit(self):
        return self.__limit
    
    def withdraw(self, amount: float) -> bool:
        """Saca um valor da conta.

        Args:
            amount (float): Valor que será sacado.

        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if self.balance + self.__limit < amount:
            return False
        
        if self.balance < amount:
            self.__limit -= amount - self.balance
            self.balance = 0
        else:
            self.balance -= amount
        
        return True
    
    def get_deposit_tax(self) -> float:
        return 0.002
    

if __name__ == "__main__":
    checking_account = CheckingAccount("William", 1000)
    checking_account.deposit(1000)
    
    checking_account.withdraw(500)
    print(checking_account)
    
    
        
