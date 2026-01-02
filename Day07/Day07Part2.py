totalTimelines = 1
beams = {}  

def splitBeams(index):
    newTimelines = 0

    try:
        newTimelines = beams[index]
    except:
        return 0
    try:
        beams[index - 1] += newTimelines
    except:
        beams[index - 1] = newTimelines
    try:
        beams[index + 1] += newTimelines
    except:
        beams[index + 1] = newTimelines
    beams.pop(index)
    return newTimelines

with open('Input.txt', 'r') as file:
    for line in file:
        if 'S' in line:
            beams[line.index('S')] = 1
        elif '^' in line:
            for index in range(0, len(line) - 1):
                if line[index] == '^':
                    try:
                        while beams[index] > 0:
                            totalTimelines += splitBeams(index)
                    except:
                        continue
                    
print("Total amount of timelines:", totalTimelines)
