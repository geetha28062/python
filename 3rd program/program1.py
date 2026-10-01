password = input("Enter password: ")

if len(password) >= 6:
    print("Valid password")
    
    encrypted = ""
    for x in password:
        encrypted += chr(ord(x) + 1)
    
    print("Encrypted:", encrypted)
else:
    print("Invalid password")