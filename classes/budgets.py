class Budget:
    def __init__(self, budget_category, budget_amount):
        self.budget_category = budget_category
        self.budget_amount = budget_amount

    def __str__(self):
        return {"b_category": self.budget_category, "b_amount": self.budget_amount}