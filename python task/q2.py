# Stored credentials
correct_username = "admin"
correct_password = "12345"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Validation
if username == correct_username:
    if password == correct_password:
        print("Login Successful!")
    else:
        print("Incorrect Password.")
else:
    print("Username does not exist.")