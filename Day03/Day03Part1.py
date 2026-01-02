total = 0

with open('Input.txt', 'r') as file:
    for line in file:
        lineTopScore = 0

        for firstIndex in range(0, len(line) - 1):
            for secondIndex in range(firstIndex + 1, len(line) - 1):
                if (int(line[firstIndex]) * 10 + int(line[secondIndex])) > lineTopScore:
                    lineTopScore = int(line[firstIndex]) * 10 + int(line[secondIndex])
        total += lineTopScore
                       
print("Total output joltage:", total)
