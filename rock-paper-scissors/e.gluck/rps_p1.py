from enum import Enum

points = {
    "X":1,
    "Y":2,
    "Z":3
}

ties = {
    "X": "A",
    "Y": "B",
    "Z": "C"

}
wins = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}


def calcScore(fileName):
    guide = open(fileName, "r")
    sum = 0
    while True:
        line = guide.readline()
        if not line:
            break
        opponentMove = line[0]
        ourMove = line[2]
        print(opponentMove)
        print(ourMove)
        sum = sum + points[ourMove]
        #tie
        if opponentMove == ties[ourMove]:
            sum = sum + 3
        #we win
        if opponentMove == wins[ourMove]:
            sum = sum + 6
    print(sum)
    guide.close()
calcScore("input.txt")