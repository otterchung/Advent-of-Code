import os

if not 'AOC2024/inputs' in os.getcwd():
    os.chdir('/Users/ahuang/Documents/Work/alan_github/Advent-of-Code/AOC2024/inputs')

newInputFile = open("1-input")
newInput = newInputFile.read()
newInputFile.close()

yourInput = """3   4
4   3
2   5
1   3
3   9
3   3"""

yourInput = newInput

line1 = []
line2 = []
for line in yourInput.split("\n"):
    x,y = line.split("   ")
    line1.append(int(x))
    line2.append(int(y))

line1.sort()
line2.sort()

part1total = 0
part2total = 0
for i in range(0,len(line1)):
    part1total += abs(line1[i] - line2[i])
    part2total += line1[i] * line2.count(line1[i])

print('Ans1:',part1total,'Ans2:',part2total)

