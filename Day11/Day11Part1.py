devices = {}
totalPaths = 0

def findPaths(fromLocation):
    pathsFound = 0

    if fromLocation == 'out':
        return 1
    for locations in devices[fromLocation]:
        pathsFound += findPaths(locations)
    return pathsFound

with open('Input.txt', 'r') as file:
    for line in file:        
        devices[line.split(': ')[0]] = ((line.split(': ')[1]).split('\n')[0]).split(' ')

totalPaths = findPaths('you')
print("Total different paths:", totalPaths)
