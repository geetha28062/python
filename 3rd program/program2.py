password = input("Enter password: ")

if any(x.isdigit() for x in password):
    print("Password contains number")
else:
    print("Add a number")