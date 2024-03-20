import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess == number:
            number_of_guesses += 1
            break
        if guess < 0 or guess > 9:
            print("Number outside range. Guess again!")
        else:
            number_of_guesses += 1

    except ValueError:
        print("Unrecognized input. Try again!")
print(f"You needed {number_of_guesses} guesses to guess the number {number}")