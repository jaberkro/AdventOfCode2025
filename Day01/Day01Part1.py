dialPointer = 50
amountsPointingAt0AfterRotation = 0

with open('Input.txt', 'r') as file:
    for line in file:
        dialPointer = dialPointer + int(line)

        if dialPointer % 100 == 0:
            amountsPointingAt0AfterRotation += 1
        while dialPointer < 0:
            dialPointer += 100
        while dialPointer > 99:
            dialPointer -= 100

print("Password:", amountsPointingAt0AfterRotation)
