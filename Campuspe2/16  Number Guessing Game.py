import random

# pick a random number and start the game
best_score = None

while True:
    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0

    print("\nHi! I am thinking of a number between 1 and 100.")
    print("You have 7 chances to guess it.")

    while attempts_left > 0:
        guess = int(input("Enter your guess: "))
        attempts_used += 1
        attempts_left -= 1

        if guess == secret_number:
            print("Great job! You guessed the correct number.")
            print("You used", attempts_used, "attempts.")

            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print("This is your best score so far!")

            break
        elif guess < secret_number:
            print("Too low. Try a bigger number.")
        else:
            print("Too high. Try a smaller number.")

        if abs(guess - secret_number) <= 5:
            print("Hint: You are very close!")

        print("Attempts remaining:", attempts_left)

    else:
        print("Oops! You did not guess the number.")
        print("The correct number was:", secret_number)

    # ask the user whether to play again
    choice = input("Do you want to play again? (yes/no): ").lower()

    if choice != "yes":
        if best_score is not None:
            print("Your best score is:", best_score, "attempts.")
        print("Thanks for playing!")
        break