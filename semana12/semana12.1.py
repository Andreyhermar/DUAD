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
    def __init__(self, balance, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"Withdrawal denied. Balance cannot go below {self.min_balance}"
            )

        return super().withdraw_money(amount)


my_account = SavingsAccount(10000, min_balance=500)

my_account.deposit_money(500)
my_account.withdraw_money(6000)

my_account.withdraw_money(1200)