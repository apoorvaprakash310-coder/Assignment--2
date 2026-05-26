# This program asks the user for several numbers and stores them in a list

n = int(input("How many numbers? "))

numbers = []

for i in range(1, n + 1):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

# This part calculates and displays sum, average, maximum and minimum

total = sum(numbers)
average = total / n

print("Sum:", total)
print("Average:", average)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))