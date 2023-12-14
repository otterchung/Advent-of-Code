import os
from copy import deepcopy

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
#data = "actual"
part1 = False #True

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "SampleInput.txt"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "Input.txt"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print("First Line: ",lines[0], "\n")

total = 0
finalString = ""
collect = []

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def splitByRange(line):
    line += "#"
    splitRange = []
    i = 0
    prev_i = 0
    y = line.count("#")
    for a in range(0, y):
        i = line.index("#", i) + 1
        splitRange.append(line[prev_i:i])
        prev_i = i
        
    return splitRange

def countLoad(ranges, start):
    total = 0
    for r in ranges:
        ohs = r.count("O")
        total += (start + start-ohs+1)/2 * ohs
        start -= len(r)
    return total

# counterclockwise rotate
def rotate(map):
    newMap = deepcopy(map)
    i = 0
    while i < len(map):
        j = 0
        while j < len(map[0]):
            newMap[len(map)-1-j][i] = map[i][j]
            j += 1
        i += 1
        
    return newMap

# clockwise rotate ("Cycle": north -> west -> south -> east -> north)
def rotateReverse(map):
    newMap = deepcopy(map)
    i = 0
    while i < len(map):
        j = 0
        while j < len(map[0]):
            newMap[j][len(map[0]) - 1 - i] = map[i][j]
            j += 1
        i += 1
        
    return newMap

def rollStones(map):
    newMap = []

    for line in map:
        line += "#"
        rollLine = []

        i = 0
        prev_i = 0
        y = line.count("#")
        for a in range(0, y):
            # ....# ""# 
            i = line.index("#", i) + 1
            
            smallRange = line[prev_i:i]
            ohs = smallRange.count("O")
            
            rollLine += ["O"] * ohs + ["."] * (len(smallRange) - ohs - 1) + ["#"]
            prev_i = i
        newMap.append(rollLine[:-1])
        
    return newMap


def doTilt(map,i):
    for i in range(0,i):
        map = rollStones(rotateReverse(map)) #west,south,east
    return map

def countVal(map):
    total = 0
    startVal = len(map)
    for line in map:
        total += line.count("O") * startVal
        startVal -= 1
    return total

map = []
for line in lines:
    map.append([x for x in line])

# print("North, Starting")
map = rollStones(rotate(map)) # now it is <--- facing "at north"

# print("Finish rotating one cycle, <-- is east")
map = doTilt(map, 3) 
#! cycle: 1

cycle = 1

cycleNum = 1000000000
maps = []
firstFind = None
breakpoint = None
while cycle < cycleNum:
    map = doTilt(map, 4)

    if firstFind == None:
        if map in maps:
            firstFind = deepcopy(map)
            firstFindCount = cycle
            print("First Cycle Found:",cycle)
        else:
            maps.append(map)
    else:
        if map == firstFind and breakpoint == None:
            cycleAmount = cycle - firstFindCount

            multiplier = int((cycleNum - firstFindCount) / cycleAmount)
            tailRemainder = cycleNum - (multiplier * cycleAmount + firstFindCount)
            breakpoint = firstFindCount + tailRemainder + cycleAmount - 1
            print("Second Cycle Found: ",cycle)
            print("Breakpoint:",breakpoint)
    if cycle == breakpoint:
        break

    if cycle % 10000 == 0:
        print(cycle)

    cycle += 1


upright = rotate(rotate(map))
startVal = len(upright)
for line in upright:
    collect.append(line.count("O") * startVal)
    startVal -= 1
    
print("Part1:",sum(collect), collect)

