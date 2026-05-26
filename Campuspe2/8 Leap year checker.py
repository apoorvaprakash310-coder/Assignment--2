# Simple and easy leap year checker

year = int(input("Enter a year: "))

# check the year using basic leap year rules

if year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year because it is divisible by 4 and not divisible by 100.")
elif year % 400 == 0:
    print(year, "is a leap year because it is divisible by 400.")
else:
    print(year, "is not a leap year because it does not follow the leap year rules.")