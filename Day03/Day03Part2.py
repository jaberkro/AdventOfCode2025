total = 0

def findHighIndex(text, minIndex, maxIndex):
    for number in range(9, 0, -1):
        try:
            index = text.index(str(number), minIndex, maxIndex)
            return index
        except ValueError:
            continue
    return minIndex

with open('Input.txt', 'r') as file:
    for line in file:
        lineTopScore = 0

        if len(line) == 0:
            break

        firstIndex = findHighIndex(line, 0, len(line) - 12)
        secondIndex = findHighIndex(line, firstIndex + 1, len(line) - 11)
        thirdIndex = findHighIndex(line, secondIndex + 1, len(line) - 10)
        fourthIndex = findHighIndex(line, thirdIndex + 1, len(line) - 9)
        fifthIndex = findHighIndex(line, fourthIndex + 1, len(line) - 8)
        sixthIndex = findHighIndex(line, fifthIndex + 1, len(line) - 7)
        seventhIndex = findHighIndex(line, sixthIndex + 1, len(line) - 6)
        eighthIndex = findHighIndex(line, seventhIndex + 1, len(line) - 5)
        ninethIndex = findHighIndex(line, eighthIndex + 1, len(line) - 4)
        tenthIndex = findHighIndex(line, ninethIndex + 1, len(line) - 3)
        eleventhIndex = findHighIndex(line, tenthIndex + 1, len(line) - 2)
        twelfthIndex = findHighIndex(line, eleventhIndex + 1, len(line) - 1)

        first = int(line[firstIndex]) * 100000000000
        second = int(line[secondIndex]) * 10000000000
        third = int(line[thirdIndex]) * 1000000000
        fourth = int(line[fourthIndex]) * 100000000
        fifth = int(line[fifthIndex]) * 10000000
        sixth = int(line[sixthIndex]) * 1000000
        seventh = int(line[seventhIndex]) * 100000
        eighth = int(line[eighthIndex]) * 10000
        nineth = int(line[ninethIndex]) * 1000
        tenth = int(line[tenthIndex]) * 100
        eleventh = int(line[eleventhIndex]) * 10
        twelfth = int(line[twelfthIndex])

        lineTopScore = first + second + third + fourth + fifth + sixth + seventh + eighth + nineth + tenth + eleventh + twelfth
        total += lineTopScore
                       
print("New total output joltage:", total)
