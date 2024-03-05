import random

answer = str(random.randint(1000,9999))
guess_count = 0

while True:
    guess = str(input("Please enter your guess: "))
    cows = 0
    bulls = 0
    for x in range(len(answer)):
        if answer[x] == guess[x]:
            cows += 1
        else:
            bulls += 1
    guess_count += 1
    if guess == answer:
        print("\nYou won in",guess_count,"guesses!")
        break
    else:
        print("Cows:",cows," Bulls:",bulls)