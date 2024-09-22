from colored import Fore, Back, Style
from classes.user import User
import json

color2: str = f"{Style.BOLD}{Fore.RED}"

def create_new_user():

    # Error handling to ensure they enter their first and last name
    name = input("\nPlease enter your first and last name: ").strip()
    while len(name.split()) != 2:
        name = input(f"{color2}Invalid:{Style.reset} Please enter your first and last name separated by a space: ")
    
    try:
        # Error handling to ensure they enter a positive and correct balance
        balance = float(input("Please enter your current bank account balance: "))
    except ValueError:
        balance = float(input(f"{color2}Invalid: {Style.reset}Please enter your current balance in numbers only: "))

        # Create new instance of user
    new_user = User(name, balance)
    # Convert to list to append to json file
    new_user_list = {"name": name, "balance": balance}
    # Open json to read
    try:
        with open("files/user_details.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = [{"name": "", "balance": 0}]
    # Add new user details
    data.append(new_user_list)
    # Update json file
    with open("files/user_details.json", "w") as file:
        json.dump(data, file, indent=4)

    return print(new_user)

    
