import json

# new_data = {
#     "name": "Chris",
#     "balance": 1500
# }

new_user_name = "Chris Apps"

try:
    with open("files/new_user.json", "r") as file:
        data = json.load(file)
        # Extract the list of names
        names_list = [user["name"] for user in data if "name" in user and user["name"]]
        if new_user_name in names_list:
            print("Already exists")
        else:
            print("User name available")
except FileNotFoundError:
    data = []

# if not isinstance(data, list):
#     data = [data]

# data.append(new_data)

# with open("files/new_user.json", "w") as file:
#     json.dump(data, file, indent=4)

# with open("files/new_user.json", "r") as file:
#         data = json.load(file)

# print(data)