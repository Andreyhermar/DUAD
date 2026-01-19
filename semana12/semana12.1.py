class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit_money(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance}")


    def withdraw_money(self, amount):
            if amount > self.balance:
                return False
            self.balance -= amount
            print(f"New balance: {self.balance}")
            return True


class SavingsAccount(BankAccount):
    def withdraw_money(self, amount):
        min_balance = 0
        success = super().withdraw_money(amount)

        if not success:
            raise ValueError(
                f"The amount withdrawn cannot exceed the current balance ({self.balance})"
            )

my_account = SavingsAccount(10000)
my_account.deposit_money(500)
my_account.withdraw_money(11000)