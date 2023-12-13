from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """SavingsAccount representa uma conta poupança."""
    interest_percentage = 0.58
    
    def generate_interest(self):
        self.balance += self.balance * (SavingsAccount.interest_percentage / 100)
    
    def get_deposit_tax(self) -> float:
        return 0.005
    
    
        
