########################## 
#  AQA User Registration #
##########################
# The program is intended to allow a user to register a new account by entering a username and password.
# • If the username has been used before then an error message is shown, and the programs ends.
# • If the username has not been used before then the password is checked to make sure that it is at least 12 characters long.
# • If the password is too short the program ends.
# • If the username and password are valid then they are displayed to the user with a success message. 

usernames = ["User1", "User2", "User3", "User4", "User5"] 

## Welcome and collect details
print("Welcome to AQA User Registration") 
username = input("New username: ")
userpassword = input("Password (12 characters or more): ")

## username already used
if username in usernames:
    print("This username is already taken.")
    exit
## userpassword length
elif len(userpassword) < 12:
    exit
else:
    print(f"Username: {username} \nPassword: {userpassword} \nYour username and password are valid.")

# # end of program 