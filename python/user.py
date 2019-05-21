class User:
    def __init__(self, name, balance):
        self.username = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print("UserName:", self.username + ", Balance:", self.balance)
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self
        
Sam = User("Sam", 150)
# Sam.make_withdrawal(50)
# Sam.display_user_balance()

Sam.make_withdrawal(50).display_user_balance()