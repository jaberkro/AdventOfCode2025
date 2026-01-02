totalFresh = 0
databaseRanges = []
rangesList = []

def reconsiderRanges():
    indexesToRemove = []

    for i in range(0, len(rangesList) - 1):
        if i in indexesToRemove:
            continue
        for j in range(i + 1, len(rangesList)):     
            if j in indexesToRemove:
                continue
            if int(rangesList[i][0]) >= int(rangesList[j][0]) and int(rangesList[i][0]) <= int(rangesList[j][1]):
                if int(rangesList[i][1]) > int(rangesList[j][1]):
                    rangesList[j][1] = rangesList[i][1]
                indexesToRemove.append(i)
            elif int(rangesList[i][1]) >= int(rangesList[j][0]) and int(rangesList[i][1]) <= int(rangesList[j][1]):
                if int(rangesList[i][0]) < int(rangesList[j][0]):
                    rangesList[j][0] = rangesList[i][0]
                indexesToRemove.append(i)
    for i in indexesToRemove:
        del rangesList[i]

with open('Database.txt', 'r') as databaseFile:
    databaseFile = sorted(databaseFile)
    for line in databaseFile:
        newRange = (line.split("\n")[0]).split("-")
        rangeUpdated = False

        for ranges in rangesList:
            if int(newRange[0]) >= int(ranges[0]) and int(newRange[0]) <= int(ranges[1]):
                if int(newRange[1]) > int(ranges[1]):
                    ranges[1] = newRange[1]
                rangeUpdated = True
                reconsiderRanges()
            elif int(newRange[1]) >= int(ranges[0]) and int(newRange[1]) <= int(ranges[1]):
                if int(newRange[0]) < int(ranges[0]):
                    ranges[0] = newRange[0]
                rangeUpdated = True
                reconsiderRanges()

        if rangeUpdated == False:
            rangesList.append(newRange)
  
    for ranges in rangesList:
        totalFresh += (int(ranges[1]) - int(ranges[0])) + 1

print("Total amount of fresh ingredient IDs:", totalFresh)
