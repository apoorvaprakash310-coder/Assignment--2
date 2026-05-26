# Movie ticket price calculator

age = int(input("Enter your age: "))
day = input("Enter day of week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# decide ticket price based on age
if age < 3:
    price = 0
elif age <= 12:
    price = 150
elif age <= 59:
    price = 300
else:
    price = 200

# apply weekend discount
if day in ["friday", "saturday", "sunday"]:
    discount = price * 0.20
else:
    discount = 0

final_price = price - discount
total = final_price * tickets

print("\nTicket price (one):", price)
print("Discount (one):", discount)
print("Final price (one):", final_price)
print("Total amount:", total)