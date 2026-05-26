# ATM program

balance = 10000
MIN_BALANCE = 500

while True:
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # user menu selection

    if choice == 1:
        print("Your balance is ₹", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print("Money added successfully")
            print("New balance: ₹", balance)
        else:
            print("Please enter a valid amount")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and balance - amount >= MIN_BALANCE:
            balance = balance - amount
            print("Withdrawal successful")
            print("New balance: ₹", balance)
        else:
            print("Not enough balance or invalid amount")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    # wrong choice entered

    else:
        print("Invalid option, try again")