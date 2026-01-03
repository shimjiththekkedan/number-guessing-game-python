import random

print("Welcome to Number Guessing Game\n")

choice = int(input("pick a option\n1. 1-100\n2. 1-50\n"))

if choice == 1:
    right_number = random.randint(1, 100)
    max_range = 100
elif choice == 2:
    right_number = random.randint(1, 50)
    max_range = 50
else:
    print("Invalid option.")
    exit()

print(f"\nI've picked a number between 1 and {max_range}.\n")

attempt = 0  # attempt = no.of guesses

while True:
    guess = int(input("Enter your guess: "))
    attempt += 1

    if guess < 1 or guess > max_range:
        print(f"Please enter a number between 1 and {max_range}.")
    elif guess > right_number:
        print("Too high. Try a lower number.\n")
    elif guess < right_number:
        print("Too low. Try a higher number.\n")
    else:
        print("\nCorrect guess!")
        print(f"You won in {attempt} attempts.")
        break