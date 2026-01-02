totalSplitted = 0
beams = []

with open('Input.txt', 'r') as file:
    for line in file:
        if 'S' in line:
            beams.append(line.index('S'))
        else:
            for index in range(0, len(line) - 1):
                if line[index] == '^' and index in beams:
                    while index in beams:
                        beams.remove(index)
                    beams.append(index - 1)
                    beams.append(index + 1)
                    totalSplitted += 1
                    
print("Total times beams splitted:", totalSplitted)
