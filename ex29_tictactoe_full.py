def draw_gameboard(width, height):              #drawing gameboard
    print("  ",end="")
    for x in range(width):                      #drawing column numbers
        print(" ",x+1,"",end = "")
    print("")
    for x in range(height):
        print("  ",end="")
        print(" ---" * width)
        print(x+1,"",end="")                    #drawing row numbers
        for y in range(width):
                if gameboard[x][y] == 0:
                    print("| - ", end="")
                if gameboard[x][y] == 1:
                    print("| X ", end="")
                if gameboard[x][y] == 2:
                    print("| O ", end="")
        print("|")
    print(" "," ---" * width)                   #drawing bottom border

def gamewin(results, count, game_done):
    for x in range(len(results)):
        if results[x][0] == results[x][1] == results[x][2] and results[x][0] > 0:       #checking row values
            print("Player " + str(results[x][0]) + " WINS")
            game_done = True
        elif results [0][x] == results[1][x] == results[2][x] and results[0][x] > 0:    #checking column values
            print("Player " + str(results[0][x]) + " WINS")
            game_done = True
        elif results[0][0] == results[1][1] == results[2][2] and results[0][0] > 0:     #checking diagonal values
            print("Player " + str(results[0][0]) + " WINS")
            game_done = True
        elif results[0][2] == results[1][1] == results[2][0] and results[0][2] > 0:     #checking diagonal values (2)
            print("Player " + str(results[0][2]) + " WINS")
            game_done = True
        elif count == 9:                                                                #checking draw
            print("DRAW")
            game_done = True
        return game_done

def game():
    counter = 0
    game_done = False
    while counter < 9:                                  #continue user input until board is filled
        if game_done == False:                          #continue user input until game is won
            while True:                                 #continue user input if move is invalid
                p1move = input("Player 1 (X) input move (row, column): ")
                p1move = p1move.split(",")
                if gameboard[int(p1move[0])-1][int(p1move[1])-1] == 0:
                    gameboard[int(p1move[0])-1][int(p1move[1])-1] = 1
                    counter += 1                        #count number of plays
                    draw_gameboard(width, height)
                    break
                else:
                    print("Try again")

            if gamewin(gameboard, counter, game_done) == True:
                break

            while True:
                p2move = input("Player 2 (O) input move (row, column): ")
                p2move = p2move.split(",")
                if gameboard[int(p2move[0])-1][int(p2move[1])-1] == 0:
                    gameboard[int(p2move[0])-1][int(p2move[1])-1] = 2
                    counter += 1
                    draw_gameboard(width, height)
                    break
                else:
                    print("Try again")

            if gamewin(gameboard, counter, game_done) == True:
                break

    print("Game is done!")

gameboard = [[0,0,0],[0,0,0],[0,0,0]]
width = int(input("Enter board width: "))
height = int(input("Enter board height: "))
draw_gameboard(width, height)
game()