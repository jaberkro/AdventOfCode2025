firstNumbers = []
secondNumbers = []
thirdNumbers = []
fourthNumbers = []
symbols = []
grandTotal = 0

with open('Input.txt', 'r') as inputFile:
    fillingIndex = 0

    for line in inputFile:
        if fillingIndex == 0:
            firstNumbers = line.split(" ")
        if fillingIndex == 1:
            secondNumbers = line.split(" ")
        if fillingIndex == 2:
            thirdNumbers = line.split(" ")
        if fillingIndex == 3:
            fourthNumbers = line.split(" ")
        if fillingIndex == 4:
            symbols = line.split(" ")
        fillingIndex += 1

firstNumbers = [s for s in firstNumbers if s]
secondNumbers = [s for s in secondNumbers if s]
thirdNumbers = [s for s in thirdNumbers if s]
fourthNumbers = [s for s in fourthNumbers if s]
symbols = [s for s in symbols if s]

for index in range(0, len(symbols)):
    if symbols[index] == '+':
        grandTotal += int(firstNumbers[index]) + int(secondNumbers[index]) + int(thirdNumbers[index]) + int(fourthNumbers[index])
    else:
        grandTotal += int(firstNumbers[index]) * int(secondNumbers[index]) * int(thirdNumbers[index]) * int(fourthNumbers[index])

print("Grand total:", grandTotal)
