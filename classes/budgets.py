class Budget:
    def __init__(self, budget_category, budget_amount):
        self.budget_category = budget_category
        self.budget_amount = budget_amount

    def __str__(self):
        return f"You have set up a {self.budget_category} budget for {self.budget_amount}."