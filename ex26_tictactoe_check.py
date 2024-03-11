results = [[0,2,1],
           [2,1,2],
           [1,0,1]]

def gamewin (results):
    for x in range(len(results)):
        print(results[x][0], results[x][1], results[x][2])
        if results[x][0] == results[x][1] == results[x][2]:
            return "Player " + str(results[x][0]) + " WINS"
        elif results [0][x] == results[1][x] == results[2][x]:
            return "Player " + str(results[0][x]) + " WINS"
        elif results[0][0] == results[1][1] == results[2][2]:
            return "Player " + str(results[0][0]) + " WINS"
        elif results[0][2] == results[1][1] == results[2][0]:
            return "Player " + str(results[0][2]) + " WINS"
    return "DRAW"

print(gamewin(results))