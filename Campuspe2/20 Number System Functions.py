# Number system program using functions and menu

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


# Armstrong number check using power of total digits

def is_armstrong(n):
    temp = n
    count = len(str(n))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10
    return total == n


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def is_perfect_number(n):
    if n <= 1:
        return False
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


def math_menu():
    while True:
        print("\n--- Number System Menu ---")
        print("1. Factorial")
        print("2. Prime check")
        print("3. Fibonacci")
        print("4. Sum of digits")
        print("5. Reverse number")
        print("6. Armstrong check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect number check")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter a number: "))
            print("Factorial =", factorial(n))

        elif choice == 2:
            n = int(input("Enter a number: "))
            print("Prime:", is_prime(n))

        elif choice == 3:
            n = int(input("Enter a number: "))
            print("Fibonacci =", fibonacci(n))

        elif choice == 4:
            n = int(input("Enter a number: "))
            print("Sum of digits =", sum_of_digits(n))

        elif choice == 5:
            n = int(input("Enter a number: "))
            print("Reversed number =", reverse_number(n))

        elif choice == 6:
            n = int(input("Enter a number: "))
            print("Armstrong:", is_armstrong(n))

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD =", gcd(a, b))

        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM =", lcm(a, b))

        elif choice == 9:
            n = int(input("Enter a number: "))
            print("Perfect number:", is_perfect_number(n))

        elif choice == 10:
            print("Program ended")
            break

        else:
            print("Invalid choice")


math_menu()