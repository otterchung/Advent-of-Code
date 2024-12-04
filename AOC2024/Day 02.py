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

def checkRow(row):
    first = True
    isIncrease = None
    i = 1
    while i < len(row):
        difference = row[i] - row[i-1]
        checkIncrease = difference > 0
        if first:
            isIncrease = difference > 0
            first = False

        if isIncrease != checkIncrease or abs(difference) > 3 or difference == 0:
            return False
        i += 1
    return True

total = 0
for line in yourInput.split("\n"):
    lineVals = [int(x) for x in line.split(" ")]

    if checkRow(lineVals):
        total += 1
    else:
        # Part 2 (else block)
        for i in range(0,len(lineVals)):
            if checkRow(lineVals[:i] + lineVals[i+1:]):
                total += 1
                break

print('Ans:',total)