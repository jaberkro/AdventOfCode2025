redTiles = []
maxRectangleSize = 0

with open('Input.txt', 'r') as file:
    for line in file:
        coordinates = line.split(',')
        redTiles.append([int(coordinates[0]), int(coordinates[1])])
        redTiles = sorted(redTiles)

for tile1 in range(0, len(redTiles) - 1):
    for tile2 in range(tile1 + 1, len(redTiles)):
        maxRectangleSize = max(maxRectangleSize, (abs(redTiles[tile1][0] - redTiles[tile2][0]) + 1) * (abs(redTiles[tile1][1] - redTiles[tile2][1]) + 1))

print("Max rectangle size:", maxRectangleSize)
