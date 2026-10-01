balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")