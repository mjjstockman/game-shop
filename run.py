import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('game_shop')


def get_customer_name():
    print("Hi! Welcome to Game Shop!\n")
    while True:
        name = input("Please enter your name:\n").lower()
        if validate_data(name):
            print("NAME IS SOOOOO SAFE!!!!")
            break

    return(name)


def validate_data(name):
    try:
        if name == "":
            raise ValueError("You must enter your name")
        else: 
            if name[0].isnumeric():
                raise ValueError("The first character of your name cannot be a number")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


cust_name = get_customer_name()



    # while True:
    #     if name is None:
    #         name = input("Please enter your name:\n").lower()
    #     elif confirm_data(name):
    #         print(f"\nThanks {name.capitalize()}! Please choose from the following:\n")
    #         break
    #     else:
    #         # print("\nInvalid choice, please try again\n")
    #         continue



# def confirm_data(data):
#     print(f"You entered {data}\n")
#     print("Is this correct?\n")
#     confirm = input("Enter Y for yes, N for No:\n")
#     confirm_strip_lcase = confirm.strip().lower()
#     if confirm_strip_lcase == "y":
#         print(f"You said {data} is correct!")
#         return True
#     elif confirm_strip_lcase == "n":
#         print("Let's try again")
#         return False
#     else:
#         print("Input must be either a Y or N")
#         return False
       

# welcome()