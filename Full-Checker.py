########################## 
#  AQA User Registration #
##########################
"""
The program is intended to allow a user to register a new account
    by entering a username and password.
• If the username has been used before then an error message is shown,
    and the programs ends.
• If the username has not been used before then the password is checked
    to make sure that it is at least 12 characters long.
• If the password is too short the program ends.
• If the username and password are valid then they are displayed to
    the user with a success message.

Amend your code from Exercise 1 so that it meets the following requirements:
• Add comments so the code is self-documenting
• When checking the username, the program should treat upper case letters
    and lower case letters as being the same. eg User1 is the same as user1
• The user is allowed 3 tries to enter a username that has not already
    been used, before the program ends
• The user is allowed 3 tries to enter a password that is at least
    12 characters long before the program ends.
• Add a text file with usernames and passwords.
    This file is read in at the beginning of the program and
    a new username and password is appended to the end of the text file
    when it has been validated.

Amend the program so that it is a fully functioning user registration system.
• Add a menu to the program, so that the user can choose between entering and
    validating an existing username and password, registering a new username and password, or quitting the program.
• Use file(s) to store username / password combinations.
• You should use modular code in your program.
"""

# getting already exsiting usernames and passwords in one string per pair, and making a list from them
def open_usernames():
    global usernames
    usernames_file = open("usernames.txt", "r+")
    usernames = usernames_file.readlines()
    # removes any spaces and capitals
    for details in usernames:
        usernames.remove(details)
        details = details.lower().strip()
        usernames.append(details)
    usernames_file.close()

# getting username and passwords as seperate items in a list from files
def seperate_details():
    global detail
    usernames_file = open("usernames.txt", "r+")
    usernames = usernames_file.read()
    # seperating items
    for details in usernames:
        detail = details.split("\n")
        detail = details.split(",")

# saving username and password to text file
def save_details():
    usernames_file = open("usernames.txt", "a")
    usernames_file.write("\n" + username + "," + password)
    usernames_file.close()

# Username and password check
def details_check():
    global password
    print("Check your exsiting details")
    # get username and password from user 
    username = input("Username: ").lower().strip()
    password = input("Password: ")
    details = username + "," + password
    # checking details 
    if details in username:
        print ("Your Username and Password are valid.")
    else:
        print ("That combination is not valid")

# loop allowing 3 attempts at the username
def username_input():
    global username
    seperate_details()
    t = 0
    a = True
    while t < 3 and a == True:
        # collect username from user
        username = input("New username: ").lower().strip()
        # check is username is already in use
        if username in detail:
            print("This username is already taken.")
            t += 1
        # exit after 3 attempts
        else:
            print("3 attempts exceeded")
            a == False

# loop to allow three attempts at the password input
def password_input():
    t = 0
    while t < 3:
        # get password input from user
        password = input("Password (12 characters or more): ")
        # checks password is at least 12 characters
        if len(password) < 12:
            t += 1
            continue
        else:
            save_details()
            # sucess message to user
            print(f"Username: {username} \nPassword: {password} \nYour username and password are valid and have been saved.")
            break


## Main Program
# Welcome message to user
print("Welcome to AQA User Registration\nMenu Options:\n1: Register\n2: Validate\n3: Exit")
T = True
# Menu option selection
while T:
    choice = input("Enter 1, 2 or 3 to proceed: ")
    # Register new password
    if choice == "1":
        print("Register a new username and password")
        username_input()
        password_input()
        T = False
    # validate exsisting details
    elif choice == "2":
        open_usernames()
        details_check()
        T = False
    # exit
    elif choice == "3":
        t = False
        exit
    # loop unless valid input
    else:
        continue


# # end of program 
