# Simple temperature converter menu

while True:

    print("\nPlease choose what you want to convert")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter your option (1–7): "))

    # asking temperature only after user selects the option
    if choice == 1:
        c = float(input("Enter Celsius value: "))
        print("Temperature in Fahrenheit:", (c * 9/5) + 32)

    elif choice == 2:
        f = float(input("Enter Fahrenheit value: "))
        print("Temperature in Celsius:", (f - 32) * 5/9)

    elif choice == 3:
        c = float(input("Enter Celsius value: "))
        print("Temperature in Kelvin:", c + 273.15)

    elif choice == 4:
        k = float(input("Enter Kelvin value: "))
        print("Temperature in Celsius:", k - 273.15)

    elif choice == 5:
        f = float(input("Enter Fahrenheit value: "))
        print("Temperature in Kelvin:", (f - 32) * 5/9 + 273.15)

    elif choice == 6:
        k = float(input("Enter Kelvin value: "))
        print("Temperature in Fahrenheit:", (k - 273.15) * 9/5 + 32)

    # stop the program
    elif choice == 7:
        print("Thank you. Program closed.")
        break

    else:
        print("Please enter a valid option")