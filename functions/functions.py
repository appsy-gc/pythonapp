from colored import Fore, Back, Style
from classes.user import User

color2: str = f"{Style.BOLD}{Fore.RED}"

def create_new_user():

    # Error handling to ensure they enter their first and last name
    name = input("\nPlease enter your first and last name: ")
    while len(name.split()) != 2:
        name = input(f"{color2}Invalid:{Style.reset} Please enter your first and last name separated by a space: ")
    
    try:
        # Error handling to ensure they enter a positive and correct balance
        balance = float(input("Please enter your current bank account balance: "))
    except ValueError:
        balance = float(input(f"{color2}Invalid: {Style.reset}Please enter your current balance in numbers only: "))

    new_user = User(name, balance)
    return print(new_user)