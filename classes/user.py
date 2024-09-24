class User:
    def __init__(self, name, balance):
        self.pro_account = False
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"\nWelcome {self.name}, thanks for creating an account and adding ${self.balance:,.2f} to it.\n"
    
class ProUser(User):
    pass