upper = 100
lower = 0
guess_count = 0
target = int(input("Please choose your number (1-100): "))

while True:
    guess = int((upper + lower) / 2)
    guess_count += 1
    print("My guess:",guess)
    assess = input(str("Is your number (H)igher / (L)ower / a (M)atch? ")).lower()
    if assess == 'h':
        lower = guess
    elif assess == 'l':
        upper = guess
    elif assess == 'm':
        break

print("It took",guess_count,"guess(es).")



