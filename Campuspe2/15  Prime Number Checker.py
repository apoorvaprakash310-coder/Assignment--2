# This program checks whether a number is prime and also prints prime numbers in a given range

num = int(input("Enter a number: "))

if num < 2:
    print(num, "is NOT a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")

# This part finds all prime numbers between the given start and end range

start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

primes = []

for n in range(start, end + 1):
    if n > 1:
        flag = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                flag = False
                break
        if flag:
            primes.append(n)

print("Prime numbers:", ", ".join(map(str, primes)))