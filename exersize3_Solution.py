########################## 
#  AQA User Registration #
##########################
"""The program is intended to allow a user to register a new account by entering a username and password.
• If the username has been used before then an error message is shown, and the programs ends.
• If the username has not been used before then the password is checked to make sure that it is at least 12 characters long.
• If the password is too short the program ends.
• If the username and password are valid then they are displayed to the user with a success message.

Amend your code from Exercise 1 so that it meets the following requirements:
• Add comments so the code is self-documenting
• When checking the username, the program should treat upper case letters and lower case letters as being the same. eg User1 is the same as user1
• The user is allowed 3 tries to enter a username that has not already been used, before the program ends
• The user is allowed 3 tries to enter a password that is at least 12 characters long before the program ends.
• Add a text file with usernames and passwords.
    - This file is to be read in at the beginning of the program and a new username and password is appended to the end of the text file when it has been validated."""

## getting already exsiting usernames and creating a list from them
usernames_file = open("usernames.txt", "r+")
usernames = usernames_file.readlines()
## removes any spaces and capitals
for name in usernames:
    name = name.lower().strip()
usernames_file.close()

# Welcome message to user
print("Welcome to AQA User Registration") 

# loop allowing 3 attempts at the username
t = 0
a = True
while t < 3 and a == True:
    # collect username from user
    username = input("New username: ").lower().strip()
    # check is username is already in use
    if username in usernames:
        t += 1
        print("This username is already taken. You have had", t, "attempts")
    # exit after 3 attempts
    else:
        print("3 attempts exceeded")
        a == False

# loop to allow three attempts at the password input
c = 0
while c < 3:
    # get password input from user
    password = input("Password (12 characters or more): ")
    # checks password is at least 12 characters
    if len(password) < 12:
        c += 1
        continue
    else:
        # adding username and password to text file
        usernames_file = open("usernames.txt", "a")
        usernames_file.write("\n" + username)
        usernames_file.close()
        password_file = open("passwords.txt", "a")
        password_file.write("\n" + password)
        password_file.close()
        # sucess message to user
        print(f"Username: {username} \nPassword: {password} \nYour username and password are valid and have been saved.")
        break

# # end of program 
