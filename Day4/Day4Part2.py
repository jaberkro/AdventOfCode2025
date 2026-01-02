totalRemoved = 0

def removeXFromGrid(grid):
    for lineIndex in range(0, len(grid)):
            for index in range(0, len(grid[lineIndex])):
                if grid[lineIndex][index] == 'x':
                    grid[lineIndex] = grid[lineIndex][:index] + '.' + grid[lineIndex][index + 1:]
    return grid

def countSurroundings(grid, lineIndex, index):
    totalSurrounding = 0
    if lineIndex > 0 and index > 0 and (grid[lineIndex - 1][index - 1] == '@' or grid[lineIndex - 1][index - 1] == 'x'):
        totalSurrounding += 1
    if lineIndex > 0 and (grid[lineIndex - 1][index] == '@' or grid[lineIndex - 1][index] == 'x'):
        totalSurrounding += 1
    if lineIndex > 0 and index < len(grid[lineIndex]) - 1 and (grid[lineIndex - 1][index + 1] == '@' or grid[lineIndex - 1][index + 1] == 'x'):
        totalSurrounding += 1
    if index > 0 and (grid[lineIndex][index - 1] == '@' or grid[lineIndex][index - 1] == 'x'):
        totalSurrounding += 1
    if index < len(grid[lineIndex]) - 1 and (grid[lineIndex][index + 1] == '@' or grid[lineIndex][index + 1] == 'x'):
        totalSurrounding += 1
    if lineIndex < len(grid) - 1 and index > 0 and (grid[lineIndex + 1][index - 1] == '@' or grid[lineIndex + 1][index - 1] == 'x'):
        totalSurrounding += 1
    if lineIndex < len(grid) - 1 and (grid[lineIndex + 1][index] == '@' or grid[lineIndex + 1][index] == 'x'):
        totalSurrounding += 1
    if lineIndex < len(grid) - 1 and index < len(grid[lineIndex]) - 1 and (grid[lineIndex + 1][index + 1] == '@' or grid[lineIndex + 1][index + 1] == 'x'):
        totalSurrounding += 1
    return totalSurrounding


with open('Input.txt', 'r') as file:
    grid = []
    grid.extend(file)
    while (totalRemoved == 0 or removedThisRound != 0):
        removedThisRound = 0
        for lineIndex in range(0, len(grid)):
            for index in range(0, len(grid[lineIndex])):
                if grid[lineIndex][index] == '@':
                    if countSurroundings(grid, lineIndex, index) < 4:
                        grid[lineIndex] = grid[lineIndex][:index] + 'x' + grid[lineIndex][index + 1:]
                        removedThisRound += 1
        totalRemoved += removedThisRound
        grid = removeXFromGrid(grid)

print("Total amount of rolls that can be removed:", totalRemoved)
