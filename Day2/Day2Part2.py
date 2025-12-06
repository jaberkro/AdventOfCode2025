total = 0

with open('Input.txt', 'r') as file:
    for line in file:
        ranges = line.split(",")
        for oneRange in ranges:
            startAndEnd = oneRange.split("-")
            for number in range(int(startAndEnd[0]), int(startAndEnd[1]) + 1, 1):
                if number > 9:
                    j = str(number)
                    sequenceSize = int(len(j) / 2)

                    while sequenceSize > 0:
                        if len(j) % sequenceSize == 0:
                            k = 0
                            while k < len(j) - sequenceSize and int(j[k:(k + sequenceSize)]) == int(j[(k + sequenceSize):(k + sequenceSize + sequenceSize)]):
                                k += sequenceSize
                            if k == len(j) - sequenceSize:
                                total += number
                                break
                        sequenceSize -= 1

print("total:", total)