# Simple calculator program using functions
# Shows a friendly menu and performs the selected operation

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


def calculator():
    while True:
        print("\nWelcome to the Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Please enter your choice (1-7): ")

        if choice == "7":
            print("Bye! Have a nice day.")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", add(a, b))
        elif choice == "2":
            print("Answer =", subtract(a, b))
        elif choice == "3":
            print("Answer =", multiply(a, b))
        elif choice == "4":
            print("Answer =", divide(a, b))
        elif choice == "5":
            print("Answer =", modulus(a, b))
        elif choice == "6":
            print("Answer =", power(a, b))
        else:
            print("Invalid choice. Please try again.")


calculator()