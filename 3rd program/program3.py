password = input("Enter password: ")

if len(password) >= 6:
    encrypted = ""
    for x in password:
        encrypted += chr(ord(x) + 1)
    print("Valid password")
    print("Encrypted:", encrypted)
else:
    print("Password too short")