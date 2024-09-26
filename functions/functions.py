from colored import Fore, Back, Style
from classes.user import User
from classes.transactions import Income, Expense
import json

color1: str = f"{Style.BOLD}{Back.GREEN}"
color2: str = f"{Style.BOLD}{Fore.RED}"

def check_user_availability():
    with open("files/user_details.json", "r") as file:
        data = json.load(file)
        user_list = [user["name"].lower().strip() for user in data if "name" in user and user["name"]]
        return user_list
    


def create_new_user():

    # Error handling to ensure they enter their first and last name
    name = input("\nPlease enter your first and last name: ").strip()
    while len(name.split()) != 2 or name.lower() in check_user_availability():
        name = input(f"{color2}Invalid: You did not enter a first and last name or your name already exists.{Style.reset}\nPlease enter your first and last name separated by a space: ")
    
    # Ensure they entered a unique name
    # if name.lower() in check_user_availability():
    #    print(f"{color2}Name in use, choose another! {Style.reset}\n")
    #    name = input("Please enter your first and last name separated by a space: ")
    # else:
    try:
        # Error handling to ensure they enter a positive and correct balance
        balance = float(input("Please enter your current bank account balance: "))
    except ValueError:
        balance = float(input(f"{color2}Invalid: {Style.reset}Please enter your current balance in numbers only: "))

    # Create new instance of user
    new_user = User(name, balance)
    new_user_data = {"pro_sub": False, "name": name, "balance": balance}

    # Commit changes to json
    try:
        with open("files/user_details.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(new_user_data)
    with open("files/user_details.json", "w") as file:
        json.dump(data, file, indent=4)

    return print(new_user)
        

def add_income():
    income = float(input("Please enter your income: "))
    new_income = Income(income)
    return print(new_income)


def add_expense():
    expense = float(input("Please enter an expense: "))
    new_expense = Expense(expense)
    return print(new_expense)


def add_budget():
    # Set up the menu for category selection
    print(f"{color1}To set up a budget, please choose one of the following categories.{Style.reset}\n")
    print("1. Food")
    print("2. Vehicle Costs")
    print("3. Bills")
    print("4. Subscriptions")
    print("5. Entertainment and games")
    print("6. Education\n")
    print(f"{color2}Note:{Style.reset} You can only choose one category for a free account. \nUpgrade back at the main menu to choose more.\n")
    # Get selection from user and set variables
    budget_category_selection = int(input("Please enter a number to choose your desired category: "))
    # Match case for selection handling
    match budget_category_selection:
        case 1:
            budget_category = "Food"
        case 2:
            budget_category = "Vehicle Costs"
        case 3:
            budget_category = "Bills"
        case 4:
            budget_category = "Subscriptions"
        case 5:
            budget_category = "Entertainment and games"
        case 6:
            budget_category = "Education"
        case _:
            print(f"\n{color2}Incorrect selection{Style.reset} - try again.\n")
            budget_category = int(input("Please enter a number to choose your desired category: "))
    # Set limit for budget
    budget_amount = float(input("What limit would you like to set for this budget per week? "))
    print(f"\n${budget_amount:,.2f} set as your limit for {budget_category}")

    return {"b_category": budget_category, "b_amount": budget_amount}


# def save_data(user_data, budget_data):
#     try:
#         with open("files/user_details.json", "r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = []  # Initialize an empty list if the file doesn't exist

#     # New data to append
#     new_data = {
#         "pro_account": False,
#         "name": user_data["name"], 
#         "balance": user_data["balance"], 
#         "b_category": budget_data["b_category"], 
#         "b_amount": budget_data["b_amount"]
#     }

#     # Append new data to the list
#     data.append(new_data)

#     # Write back to the JSON file
#     with open("files/user_details.json", "w") as file:
#         json.dump(data, file, indent=4)

#     print("Saved. Goodbye")
