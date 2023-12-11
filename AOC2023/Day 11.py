import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
data = "actual"
part1 = False #True

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

nodes = []
galRow = []

i = 0
while i < len(lines):
    j = 0
    galRowBool = True
    while j < len(lines[i]):


        if lines[i][j] == "#":
            nodes.append([i,j])
            galRowBool = False
        j += 1

    if galRowBool:
        galRow.append(i)
    i += 1
    
j = 0
galCol = []
while j < len(lines[0]):
    i = 0
    galColBool = True
    while i < len(lines):
        if lines[i][j] == "#":
            galColBool = False
        i += 1
    if galColBool:
        galCol.append(j)
    j += 1

distances = 0
expand = 1000000-1
for node in nodes:
    
    for node2 in nodes:
        distance = abs(node[0] - node2[0]) + abs(node[1] - node2[1])

        for x in range(node[0], node2[0]):
            if x in galRow:
                distance += expand
        for y in range(node[1],node2[1]):
            if y in galCol:
                distance += expand

        for x in range(node2[0], node[0]):
            if x in galRow:
                distance += expand
        for y in range(node2[1],node[1]):
            if y in galCol:
                distance += expand
        distances += distance

print(distances/2)

#271514131521.0
# 82000210.0