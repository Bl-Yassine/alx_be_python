class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        
    def withdraw(self, amount):
        try: 
            if amount - self.account_balance >= 0:
                self.account_balance -= amount
                return True
        except:
                return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

        



