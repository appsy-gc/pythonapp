from colored import Fore, Back, Style
from classes.user import User
import json

color2: str = f"{Style.BOLD}{Fore.RED}"

def check_user_availability():
    with open("files/user_details.json", "r") as file:
        data = json.load(file)
        user_list = [user["name"].lower().strip() for user in data if "name" in user and user["name"]]
        return user_list
    


def create_new_user():

    # Error handling to ensure they enter their first and last name
    name = input("\nPlease enter your first and last name: ").strip()
    while len(name.split()) != 2:
        name = input(f"{color2}Invalid:{Style.reset} Please enter your first and last name separated by a space: ")
    
    # Ensure they entered a unique name
    if name.lower() in check_user_availability():
        print(f"{color2}Name in use, choose another!{Style.reset}")

    else:
        try:
            # Error handling to ensure they enter a positive and correct balance
            balance = float(input("Please enter your current bank account balance: "))
        except ValueError:
            balance = float(input(f"{color2}Invalid: {Style.reset}Please enter your current balance in numbers only: "))

        # Create new instance of user
        new_user = User(name, balance)
        # Convert to list to append to json file
        new_user_list = {"pro_account": False, "name": name, "balance": balance}
        
        # Open json to read
        try:
            with open("files/user_details.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = [{"pro_account": False, "name": "", "balance": 0}]
        # Add new user details
        data.append(new_user_list)
        # Update json file
        with open("files/user_details.json", "w") as file:
            json.dump(data, file, indent=4)
        
        return print(new_user)
        
def add_income():
    pass

def add_expense():
    pass

def add_budget():
    pass

    
