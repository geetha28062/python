balance = 5000
pin = 1234

p = int(input("Enter PIN: "))

if p == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("Deposited successfully")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice")
else:
    print("Wrong PIN")