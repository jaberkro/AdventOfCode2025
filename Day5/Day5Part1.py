totalFresh = 0
database = {}
rangesList = []

with open('TestDatabase.txt', 'r') as databaseFile:
    for line in databaseFile:
        ranges = line.split("-")
        rangesList.append(ranges)

with open('TestInput.txt', 'r') as inputFile:
    for line in inputFile:
        for ranges in rangesList:
            if int(ranges[0]) <= int(line) and int(ranges[1]) >= int(line):
                totalFresh += 1    
                break

print("Total amount of fresh ingredient IDs:", totalFresh)
