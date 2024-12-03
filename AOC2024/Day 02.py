import os

if not 'AOC2024/inputs' in os.getcwd():
    os.chdir('/Users/ahuang/Documents/Work/alan_github/Advent-of-Code/AOC2024/inputs')

newInputFile = open("2-input")
newInput = newInputFile.read()
newInputFile.close()

yourInput = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

yourInput = newInput

total = 0
for line in newInput.split("\n"):
    row = [int(x) for x in line.split(" ")]

    i = 1
    first = True
    isIncrease = None
    isSafe = True

    while i < len(row):
        difference = row[i] - row[i-1]
        checkIncrease = difference > 0
        if first:
            isIncrease = difference > 0
            first = False
        if isIncrease != checkIncrease or abs(difference) > 5 or difference == 0:
            isSafe = False
            i = len(row)
        i += 1
    if isSafe:
        total += 1
print('Ans:',total)