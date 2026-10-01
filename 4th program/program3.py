contacts = {"dhanu": "9876543210", "anu": "9876501234"}

name = input("Enter name: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")