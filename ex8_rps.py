def rps_win(a,b):
    if a == b:
        print("Draw!")
    elif a == 'r' and b == 's':
        print("Player 1 wins!")
    elif a == 'p' and b == 'r':
        print("Player 1 wins!")
    elif a == 's' and b == 'p':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

while True:
    player1 = str(input("<Player 1> Choose (r)ock (p)aper (s)cissors: ").lower())
    player2 = str(input("<Player 2> Choose (r)ock (p)aper (s)cissors: ").lower())
    rps_win(player1,player2)
    if input("Play again? y/n ") == 'n':
        break
