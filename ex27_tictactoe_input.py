gameboard = [[0,0,0],
             [0,0,0],
             [0,0,0]]
counter = 0

def print_moves(gameboard):
   for x in range(3):
       for y in range(3):
            if gameboard[x][y] == 0:
                print(" - ", end="")
            elif gameboard[x][y] == 1:
                print(" X ", end="")
            elif gameboard[x][y] == 2:
                print(" O ", end="")
       print("\n")

while counter < 9:
    while True:
        p1move = input("Player 1 (X) input move (row, column): ")
        p1move = p1move.split(",")
        if gameboard[int(p1move[0])-1][int(p1move[1])-1] == 0:
            gameboard[int(p1move[0])-1][int(p1move[1])-1] = 1
            counter += 1
            print_moves(gameboard)
            break
        else:
            print("Try again")

    while True:
        p2move = input("Player 2 (X) input move (row, column): ")
        p2move = p2move.split(",")
        if gameboard[int(p2move[0])-1][int(p2move[1])-1] == 0:
            gameboard[int(p2move[0])-1][int(p2move[1])-1] = 2
            counter += 1
            print_moves(gameboard)
            break
        else:
            print("Try again")

print("Game is done!")