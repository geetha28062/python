contacts = {"Ram": "9876543210", "John": "9876501234"}

name = input("Enter name: ")

if name in contacts:
    del contacts[name]
    print("Contact deleted")
else:
    print("Contact not found")