machines = []
total = 0

def pressButton(currentLights, button):
    lightsToToggle = button.split(',')
    newLights = ''

    for lightIndex in range (0, len(currentLights)):
        for light in lightsToToggle:
            if lightIndex == int(light):
                if currentLights[lightIndex] == '.':
                    newLights += '#'
                else:
                    newLights += '.'
        if len(newLights) < lightIndex + 1:
            newLights += currentLights[lightIndex]
    return newLights

def findButtonCombination(lightsGoal, currentLights, buttons, buttonIndex, amountButtonsPressed):
    minButtonsPressed = 2147483647

    if currentLights == lightsGoal:
        return amountButtonsPressed
    elif buttonIndex < len(buttons):
        buttonsPressed = findButtonCombination(lightsGoal, pressButton(currentLights, buttons[buttonIndex][1:-1]), buttons, buttonIndex + 1, amountButtonsPressed + 1)
        if buttonsPressed != -1 and buttonsPressed < minButtonsPressed:
            minButtonsPressed = buttonsPressed

        buttonsPressed = findButtonCombination(lightsGoal, currentLights, buttons, buttonIndex + 1, amountButtonsPressed)
        if buttonsPressed != -1 and buttonsPressed < minButtonsPressed:
            minButtonsPressed = buttonsPressed
        if minButtonsPressed != 2147483647:
            return minButtonsPressed
    return -1

with open('Input.txt', 'r') as file:
    for line in file:        
        machines.append([(line.split('] ')[0])[1:], ((line.split('] ')[1]).split(' {')[0]).split(' ')])

for machine in machines:
    lightsGoal = machine[0]
    currentLights = machine[0].replace('#', '.')
    buttonPresses = findButtonCombination(lightsGoal, currentLights, machine[1], 0, 0)
    total += buttonPresses

print("Total:", total)
