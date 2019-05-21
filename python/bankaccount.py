class BankAccount:
    interestamount = 0
    def __init__(self, balance, interest):
        if balance != 0:
            self.balance = balance
        else:
            self.balance = 0
        self.interest = (interest * .01)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= (amount + 5)
        return self

    def display_account_info(self):
        print("Balance: $" +  str(self.balance))
        return self

    def yield_interest(self):
        interestamount = (self.balance * self.interest)
        if balance > 0:
            balance += interestamount
        return self

Sam = BankAccount(150, 1)
Sam.deposit(100).deposit(100).deposit(100).withdraw(100).display_account_info()