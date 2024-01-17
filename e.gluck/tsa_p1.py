import re
regex = "-?\d+"

class Star:
    def __init__(self, xPos, yPos, xVel, yVel):
        self.xPos = xPos
        self.yPos = yPos

def visualizer(fileName):
    input = open(fileName, "r")
    while True:
        line = input.readline()
        if not line:
            break
        print(re.findall(regex, line))
    input.close()
visualizer("input.txt")