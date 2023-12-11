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

i = 0
start = None
newMap = []

while i < len(lines):
    j = 0
    newMap.append([""] * len(lines) * 2)
    newMap.append([""] * len(lines) * 2)
    #newMap.append([""] * len(lines) * 3)

    while j < len(lines[i]):
        if lines[i][j] == "S":
            start = i,j
        
        #if lines[i][j] == ".":
        newMap[2*i+1][2*j+1] = "."
        j += 1

    i += 1



singleLine = "*" * len(lines[0])
allLines = "\n".join([singleLine] * len(lines))

def findFirstPoss(map, current, previous):

    #! Part 2
    x0, y0 = current[0] * 2, current[1] * 2
    newMap[x0][y0] = "S"
    newMap[x0+1][y0+1] = ""

    poss = [(0,1),(0,-1),(1,0),(-1,0)]
    pipes = "-7|JLSF"
    i,j = current
    for delta_x,delta_y in poss:
        x,y = i + delta_x, j + delta_y
        next = x,y

        if x >= len(lines) or y >= len(lines[x]) or x < 0 or y < 0:
            continue 

        #print("hello", next, previous, x, y)
        if next != previous and map[x][y] in pipes:
            tile = map[x][y]

            #! Part 2
            x1, y1 = x * 2, y * 2
            xhalf, yhalf = int(x0 + (x1-x0)/2), int(y0 + (y1-y0)/2)

            if x1-x0 == 0:
                newMapTile = "-"
            else:
                newMapTile = "|"
            newMap[xhalf][yhalf] = newMapTile
            #! ----

            #print(next, previous, current, tile)
            previous = current
            return next, previous, tile
    print('crap, start')

def findNext(map, current, previous, tile):
    pipeDirection = {
        "-": [(0,1),(0,-1)],
        "7": [(0,-1),(1,0)],
        "|": [(1,0),(-1,0)],
        "J": [(0,-1),(-1,0)],
        "L": [(-1,0),(0,1)],
        #"S": [],
        "F": [(1,0),(0,1)],
    }

    poss = pipeDirection[tile]
    i,j = current

    #! Part 2
    x0, y0 = current[0] * 2, current[1] * 2
    newMap[x0][y0] = tile
    newMap[x0+1][y0+1] = ""

    for delta_x,delta_y in poss:
        x,y = i + delta_x, j + delta_y
        next = x,y
    
        if x >= len(lines) or y >= len(lines[x]) or x < 0 or y < 0:
            continue 
        
        if next != previous:
            tile = map[x][y]

            #! Part 2
            x1, y1 = x * 2, y * 2
            xhalf, yhalf = int(x0 + (x1-x0)/2), int(y0 + (y1-y0)/2)

            if x1-x0 == 0:
                newMapTile = "-"
            else:
                newMapTile = "|"
            newMap[xhalf][yhalf] = newMapTile
            #! ----

            #allLines[x][y] = "#"
            #print(next, previous, current, tile)
            previous = current
            return next, previous, tile
    print('crap')


previous = None
length = 0
current = start

tile = 'S'
next, previous, nextTile = findFirstPoss(lines, current, previous)

pathing = []
pathing.append(current)

while nextTile != 'S':
    
    # if length < 20:
    #     print(tile, previous, next, nextTile)

    tile = nextTile
    current = next
    
    next, previous, nextTile = findNext(lines, current, previous, nextTile)
    pathing.append(current)
    
    # Part 2
    x0, y0 = previous 
    x1, y1 = next



    #current = cur
    #previous = prev

    length += 1
    #print(tile, length)
    #print(previous, current)
pathing.append(next)



    
print('end',tile, previous, next, nextTile)

print("P1 Answer: ",length/2)

#p1 - 6812

# Part 2 Logic (thanks Robin)
isInside = 0
for row in newMap:
    countFlats = 0
    for j in range(0,len(row)):
        if row[j] == "|":
            countFlats += 1
        if row[j] == "." and countFlats % 2 == 1:
            row[j] = "I"
            isInside += 1
print("P2 Answer:",isInside)

#141
#451
#1391 too high

oldCount = 0
for line in lines:
    for x in line:
        if x == ".":
            oldCount += 1

newCount = 0
for line in newMap:
    for x in line:
        if x == ".":
            newCount+=1

print(oldCount, newCount)

# for x in newMap:
#     print("\t".join([y for y in x]))