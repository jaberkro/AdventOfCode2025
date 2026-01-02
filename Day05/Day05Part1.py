totalFresh = 0
rangesList = []

with open('Database.txt', 'r') as databaseFile:
    for line in databaseFile:
        ranges = line.split("-")
        rangesList.append(ranges)

with open('Input.txt', 'r') as inputFile:
    for line in inputFile:
        for ranges in rangesList:
            if int(ranges[0]) <= int(line) and int(ranges[1]) >= int(line):
                totalFresh += 1    
                break

print("Total amount of fresh ingredient IDs:", totalFresh)
