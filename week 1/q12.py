class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        self.dep_amount = int(input("Enter amount to deposit: "))
        self.balance += self.dep_amount

    def withdrawal(self):
        self.withd_amount = int(input("Enter amount to withdrwa: "))
        if self.balance < self.withd_amount:
            print("Insufficient funds")
        else:
            print("Withdrawal is successful")
            self.balance -= self.withd_amount
            print(f"{self.withd_amount} withdrawn. New balance: {self.balance}")

    def displayBalance(self):
        print(f"Your current balance is: {self.balance}")


class SavingsAccount(BankAccount):
    interest_rate = 0.05  # 5% annual interest

    def deposit(self):  # override the deposit()
        super().deposit()
        # Simple interest = Principal Amount (Deposit) x Interest Rate x Time
        interest_earned = self.balance * self.interest_rate * 1
        self.balance += interest_earned
        print(f"Interest earned on deposit: {interest_earned:.2f}")


bank_account = BankAccount()
print("\n____Bank account details____\n")
bank_account.displayBalance()
bank_account.deposit()
bank_account.displayBalance()
bank_account.withdrawal()
bank_account.displayBalance()

savings_account = SavingsAccount()
print("\n____Saving account details____\n")
savings_account.displayBalance()
savings_account.deposit()
savings_account.displayBalance()
