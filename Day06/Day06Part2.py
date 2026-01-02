worksheet = []
grandTotal = 0

with open('Input.txt', 'r') as inputFile:
    for line in inputFile:
        worksheet.append(line)

index = len(worksheet[0]) - 2
while index >= 0:
    numbers = []

    while worksheet[-1][index] == ' ':
        number = 0

        for y in range(0, 4):
            if worksheet[y][index] != ' ':
                number = number * 10 + int(worksheet[y][index])
        numbers.append(number)
        index -= 1

    number = 0
    for y in range(0, 4):
        if worksheet[y][index] != ' ':
            number = number * 10 + int(worksheet[y][index])
    numbers.append(number)

    total = 0
    if worksheet[-1][index] == '+':
        for number in numbers:
            total += number
    elif worksheet[-1][index] == '*':
        total = 1
        for number in numbers:
            total *= number
    grandTotal += total
    index = index - 2

print("Grand total:", grandTotal)
