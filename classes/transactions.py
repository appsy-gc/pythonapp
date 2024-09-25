# Parent class
class Transaction:
    def __init__(self, amount):
        self.amount = amount

# Child class for Income
class Income(Transaction):
    def __init__(self, income):
        # Pass the income amount to the parent class
        super().__init__(income)  

    def __str__(self):
        return f"You have added ${self.amount:,.2f} to your account."

# Child class for Expense
class Expense(Transaction):
    def __init__(self, expense):
        # Pass the expense amount to the parent class
        super().__init__(expense)  

    def __str__(self):
        return f"You have add a ${self.amount:,.2f} expense to your account."