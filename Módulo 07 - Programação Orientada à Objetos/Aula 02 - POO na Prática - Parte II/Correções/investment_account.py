from bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """InvestmentAccount representa uma conta de investimento."""    
    interest_percentage = 0.8
    
    def __init__(self, holder: str):
        super().__init__(holder)
        self.__amount_invested = 0
    
    def get_deposit_tax(self) -> float:
        return 0.008
    
    def invest_in_shares(self, amount: float):
        if (self.withdraw(amount)):
            self.__amount_invested += amount
            
    def generate_interest(self):
        self.balance += self.__amount_invested * (InvestmentAccount.interest_percentage / 100)
    
        
    
    
        
