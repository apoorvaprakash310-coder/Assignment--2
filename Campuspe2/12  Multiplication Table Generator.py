# ask the user for the number and the ending range
number = int(input("Enter number: "))
end = int(input("Enter range (end): "))

print("\nMultiplication Table of", number)

# show the table from 1 to the given range
for i in range(1, end + 1):
    print(f"{number} x {i} = {number * i}")