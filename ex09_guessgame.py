import random

def guess_parse(guess, target):
    if guess == target:
        print("That's it!")
    if guess > target:
        print("Guess lower.")
    if guess < target:
        print("Guess higher.")

target = random.randint(0,100)
guess_count = 0
again = 'y'

while again == 'y':
    guess = int(input("Enter your number: "))
    guess_parse(guess, target)
    guess_count += 1
    if guess == target:
        print(f"It took you {guess_count} guesses.")
        again = input("Play again? y/n ").lower()
        target = random.randint(0, 100)
        guess count = 0
