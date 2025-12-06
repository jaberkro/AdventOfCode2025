total = 0

with open('Input.txt', 'r') as file:
    for line in file:
        ranges = line.split(",")
        for oneRange in ranges:
            startAndEnd = oneRange.split("-")
            for number in range(int(startAndEnd[0]), int(startAndEnd[1]) + 1):
                if number > 9:
                    j = str(number)
                    half = int(len(j) / 2)

                    if len(j) % 2 == 0 and int(j[:half]) == int(j[half:]):
                        total += number

print("total:", total)