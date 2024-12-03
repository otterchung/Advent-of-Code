import os

if not 'AOC2024/inputs' in os.getcwd():
    os.chdir('/Users/ahuang/Documents/Work/alan_github/Advent-of-Code/AOC2024/inputs')

newInputFile = open("3-input")
newInput = newInputFile.read()
newInputFile.close()

# Sample Input
yourInput = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Given Input
yourInput = newInput

search = "mul("
prevStart = -1
total = 0

i = 0
while i >= prevStart:
    nextFind = yourInput.find(search, i)

    #Part 2
    nextDont = yourInput.find("don't()",i)
    if nextDont < nextFind and nextDont != - 1:
        i = yourInput.find("do()", nextDont)
        continue        

    i = nextFind + len(search)

    num1 = ""
    # next time use String.isdigit()
    while yourInput[i] in "0123456789":
        num1 += yourInput[i]
        i += 1

    if yourInput[i] != ",":
        continue
    i += 1

    num2 = ""
    while yourInput[i] in "0123456789":
        num2 += yourInput[i]
        i += 1

    if yourInput[i] != ")":
        continue
    
    i += 1
    prevStart = i
    total += int(num1) * int(num2)
    print("Found", num1, num2, i)

print("Ans", total)
# too low 7214400
# too low 86056442
# 174336360 too high