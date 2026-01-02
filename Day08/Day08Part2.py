import math
from operator import itemgetter

boxes = []
distances = []
circuits = []

def isLastAdded():
    for distance in distances:
        if distance[0] not in circuits[0] or distance[1] not in circuits[0]:
            return False
    return True

def mergeCircuits(newFrom, newTo, circuitIndex):
    for i in range(len(circuits) - 1, circuitIndex, -1):
        while i > circuitIndex and i < len(circuits) and (newFrom in circuits[i] or newTo in circuits[i]):
            for boxIndex in circuits[i]:
                if boxIndex not in circuits[circuitIndex]:
                    circuits[circuitIndex].append(boxIndex)
            circuits.pop(i)

def addToCircuits(newFrom, newTo):
    addedToCircuit = False

    for i in range(0, len(circuits)):
        if i < len(circuits) and newFrom in circuits[i] and newTo in circuits[i]:
            return
        elif i < len(circuits) and newFrom in circuits[i] and newTo not in circuits[i]:
            circuits[i].append(newTo)
            addedToCircuit = True
            if i < len(circuits):
                mergeCircuits(newFrom, newTo, i)
                i -= 1
                if i < 0: 
                    i = 0
        elif i < len(circuits) and newTo in circuits[i] and newFrom not in circuits[i]:
            circuits[i].append(newFrom)
            addedToCircuit = True
            if i < len(circuits):
                mergeCircuits(newFrom, newTo, i)
                i -= 1
                if i < 0: 
                    i = 0
        if isLastAdded():
            return
    if addedToCircuit == False:
        circuits.append([newFrom, newTo])

def calculateDistance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow(int(x1) - int(x2), 2) + pow(int(y1) - int(y2), 2) + pow(int(z1) - int(z2), 2))

with open('Input.txt', 'r') as file:
    for line in file:
        boxes.append((line.split('\n')[0]).split(','))

for i in range (0, len(boxes) - 1):
    for j in range (i + 1, len(boxes)):
        distances.append([i, j, calculateDistance(boxes[i][0], boxes[i][1], boxes[i][2], boxes[j][0], boxes[j][1], boxes[j][2])])

distances = sorted(distances, key=itemgetter(2))

for distance in distances:
    addToCircuits(distance[0], distance[1])
    if isLastAdded():
        print("X coordinates of last junction boxes multiplied by each other:", int(boxes[distance[0]][0]) * int(boxes[distance[1]][0]))
        break
