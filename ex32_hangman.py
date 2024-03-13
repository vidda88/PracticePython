import random

def choose_word():                                  #select a random word from list
    with open("sowpods.txt") as open_file:
        word_list = open_file.readlines()
    answer = random.choice(word_list)
    answer = answer.strip()
    return answer

def check_word(progress, guess, answer):            #check if guess letter in word
    for x in range(len(progress)):
        if guess == answer[x]:
            progress[x] = answer[x]                 #set blanks to guess letter (if correct)
    return progress

def hangman_game():
    again = 'Y'
    while again == 'Y':
        answer = list(choose_word())                #choose word
        wrong_guess = 6
        guess_count = 0
        guess_list = set()                          #initialize guess letter tracker
        progress = list('_' * len(answer))
        print("Welcome to HANGMAN! Let's play!")
        while progress != answer and wrong_guess > 0:           #ask for input until game done
            print(*progress)
            print(wrong_guess,"wrong guess(es) remaining.",end=" ")
            print("Guessed letters:",str("".join(sorted(guess_list))))
            guess = input("Please guess a letter: ").upper()
            while guess in guess_list:                          #ensure same letternot already guessed
                guess = input("You've already guessed that. Please guess again: ").upper()
            guess_list.add(guess)
            progress = check_word(progress, guess, answer)
            guess_count += 1
            if guess not in answer:                             #word guess decrement if wrong
                wrong_guess -= 1
        if progress == answer:
            print("That's right! It was " + str("".join(answer)) + ".")
            print("You won in " + str(guess_count) + " guess(es).")
        else:
            print("You used all your guesses.")
            print("The word was " + str("".join(answer)) + ".")
        again = input("Would you like to play again? Y/N ").upper()

hangman_game()