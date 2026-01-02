previousDialPointer = 50
dialPointer = 50
amountsPointingAt0AfterRotation = 0
amountsPointingAt0DuringRotation = 0

with open('Input.txt', 'r') as file:
    for line in file:
        dialPointer = dialPointer + int(line)

        if dialPointer % 100 == 0:
            amountsPointingAt0AfterRotation += 1
        while dialPointer < 0:
            if previousDialPointer != 0:
                amountsPointingAt0DuringRotation += 1
            dialPointer += 100
            previousDialPointer = dialPointer
        while dialPointer > 99:
            if dialPointer != 100:
                amountsPointingAt0DuringRotation += 1
            dialPointer -= 100
        previousDialPointer = dialPointer

print("Password:", amountsPointingAt0AfterRotation + amountsPointingAt0DuringRotation)
