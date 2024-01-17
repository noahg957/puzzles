from enum import Enum

points = {
    "A":1,
    "B":2,
    "C":3
}

ties = {
    "A": "A",
    "B": "B",
    "C": "C"
}

wins = {
    "C": "A",
    "A": "B",
    "B": "C"
}
losses = {
    "A": "C",
    "B": "A",
    "C": "B"
}


def calcScore(fileName):
    guide = open(fileName, "r")
    sum = 0
    while True:
        line = guide.readline()
        if not line:
            break
        opponentMove = line[0]
        result = line[2]
        #we lose
        if result == "X": 
            ourMove = losses[opponentMove]
            #points for choosing a move
            sum = sum + points[ourMove]
            #no points for loss
            sum = sum + 0
         #we tie
        if result == "Y": 
            ourMove = ties[opponentMove]
            #points for choosing a move
            sum = sum + points[ourMove]
            #points for draw
            sum = sum + 3
         #we win
        if result == "Z": 
            ourMove = wins[opponentMove]
            #points for choosing a move
            sum = sum + points[ourMove]
            #points for win
            sum = sum + 6
    print(sum)
    guide.close()
calcScore("input.txt")