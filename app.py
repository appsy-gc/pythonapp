# Import libraries
from colored import Fore, Back, Style
from classes.user import User
from functions.functions import create_new_user

color1: str = f"{Style.BOLD}{Back.GREEN}"
color2: str = f"{Style.BOLD}{Fore.RED}"

# Create welcome message
def create_menu():
    print(f"\n{color1}Welcome to your personal budgeting App.{Style.reset}")
    print(f"{color1}Here are your options:{Style.reset}\n")

    # Build user interface
    print("1. Create an account")
    print("2. Add income")
    print("3. Set or change a budget")
    print("4. Add an expense")
    print("5. Check a budget\n")

    print(f"{color1}<<< ADVANCED OPTIONS FOR PRO USERS >>>{Style.reset}\n")

    print("6. Import financial information with a csv file")
    print("7. Print financial graph\n")

    print(f"{color1}<<< Other Options >>>{Style.reset}\n")

    print("8. Upgrade to PRO")
    print("9. Quit the app\n")

    choice = input("Select an option to get started: ")
    return choice

choice = ""

while choice != "9":
    choice = create_menu()

    # Match block to handle choices
    match choice:
        case "1":
            # Function to get user input and creates instance of User class
            create_new_user()
            # Pause to get option selection again from user
            choice = input("\nWhat would you like to do next? ")
        case "2":
            print("2. Add income")
        case "3":
            print("3. Set a budget")
        case "4":
            print("4. Add an expense")
        case "5":
            print("5. Check a budget")
        case "6":
            print("6. Import financial information with a csv file")
        case "7":
            print("7. Print financial graph")
        case "8":
            print("8. Upgrade to PRO")
        case "9":
            print("Goodbye meat bag...")
        case _:
            print(f"{color2}Incorrect selection, try again.{Style.reset}")

# Goodbye 
print("\nThank you for choosing this shitty app.\n")