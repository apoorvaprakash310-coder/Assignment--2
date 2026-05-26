# This program helps you find the factorial of a number in a simple way

number = int(input("Please enter any number: "))

if number < 0:
    print("Sorry, factorial is not possible for negative numbers.")
elif number == 0:
    print("0! = 1")
else:
    answer = 1
    steps = []

    # This loop multiplies the numbers and prepares the step-by-step output
    for i in range(number, 0, -1):
        answer = answer * i
        steps.append(str(i))

    print(f"{number}! = " + " x ".join(steps) + f" = {answer}")