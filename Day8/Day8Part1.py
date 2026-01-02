import math
from operator import itemgetter

connectionsToMake = 1000
circuits = []
boxes = []
distances = []
circuitsizes = []

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
        if i < len(circuits) and newFrom in circuits[i] and newTo not in circuits[i]:
            circuits[i].append(newTo)
            addedToCircuit = True
            if i < len(circuits) - 1:
                mergeCircuits(newFrom, newTo, i)
        elif i < len(circuits) and newTo in circuits[i] and newFrom not in circuits[i]:
            circuits[i].append(newFrom)
            addedToCircuit = True
            if i < len(circuits) - 1:
                mergeCircuits(newFrom, newTo, i)
    if addedToCircuit == False:
        newCircuit = [newFrom, newTo]
        circuits.append(newCircuit)

def calculateDistance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow(int(x1) - int(x2), 2) + pow(int(y1) - int(y2), 2) + pow(int(z1) - int(z2), 2))

with open('Input.txt', 'r') as file:
    for line in file:
        boxes.append(line.split(','))

for i in range (0, len(boxes) - 1):
    for j in range (i + 1, len(boxes)):
        distanceMeasurement = [i, j, calculateDistance(boxes[i][0], boxes[i][1], boxes[i][2], boxes[j][0], boxes[j][1], boxes[j][2])]
        distances.append(distanceMeasurement)

distances = sorted(distances, key=itemgetter(2))

for i in range(0, 1000):
    if i > len(distances):
        break
    addToCircuits(distances[i][0], distances[i][1])

for circuit in circuits:
    circuitsizes.append(len(circuit))

circuitsizes = sorted(circuitsizes)
print("Total:", circuitsizes[-1] * circuitsizes[-2] * circuitsizes[-3])
