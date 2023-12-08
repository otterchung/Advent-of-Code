import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
data = "actual"
part1 = False

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "SampleInput.txt"
    instr = "LR"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "Input.txt"
    instr = "LRLRRLLRRLRLRRLLRRLRRLLRRLRRRLRRLRRLRRRLRRLRLRLRLLLRRRLRLLRRLRLRRRLRRLLRRLRRRLRRLRLRLRRRLRLRRRLLRLLRRLRRRLLRRLRLLLRRLRLRLLRRLRLRRRLLRLLRRRLRLLRRRLRRLRRLRRRLRRRLLRLLRRRLRRRLRRLRRRLLRRRLRLRRLLRRLRLRLRRLRRLRLLRRRLRRRLLLRLRLRRRLLRRLRRRLRLRRLLRRLRRLLRLRLRRRLRLRLRLRRRLRLLRRRLRRRLRRLLLRRRR"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print("First Line: ",lines[0], "\n")

total = 0
finalString = ""
collect = []

startNodes = []
directions = dict()
for line in lines:
    node, lrArr = line.split(" = ")
    directions[node] = lrArr.strip("()").split(", ")
    if node[2] == 'A':
        startNodes.append(node)

if part1:
    startNodes = ["AAA"]
i = 0

j = 0
pathCount = []
paths = []
for node in startNodes:
    start = node
    path = [node]
    notDone = True
    while notDone:

        for lr in instr:
            if lr == "L":
                newNode = directions[node][0]
            else:
                newNode = directions[node][1]

            if (newNode[2] == 'Z' and not part1) or (newNode == 'ZZZ' and part1):
                notDone = False
                path.append(newNode)
                paths.append(path)
                break
            
            path.append(newNode)
            node = newNode

from math import lcm
lcmValue = 1
for p in paths:
    #print(p[0],p[-1], len(instr), (len(p)-1), (len(p)-1)/len(instr), directions[p[-1]][1])
    # the answer would be the 4th column
    # the answer for part 2 is the LCM of all column 4s
    lcmValue = lcm(lcmValue, len(p)-1)
print("Answer:",lcmValue)