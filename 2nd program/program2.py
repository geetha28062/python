balance = 5000

print("ATM")
print("1. Check Balance")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Your balance is:", balance)
else:
    print("Invalid choice")