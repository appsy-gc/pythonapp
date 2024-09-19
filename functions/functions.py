from classes.user import User

def create_new_user():
    # Error handling to ensure they enter their full name
    # Error handling to ensure they enter a positive and correct balance
    # Format balance so it looks like financial data. E.g., $##,###.##
    name = input("\nPlease enter your full name: ")
    balance = int(input("Please enter your current bank account balance $: "))

    new_user = User(name, balance)
    return print(new_user)