class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"\nWelcome {self.name}, thanks for creating an account and adding ${self.balance} to it.\n"