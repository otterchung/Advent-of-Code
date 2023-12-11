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
    newMap.append([" "] * len(lines) * 2)
    newMap.append([" "] * len(lines) * 2)

    while j < len(lines[i]):
        if lines[i][j] == "S":
            start = i,j

        #! Setting the offset for expanded map tiles
        newMap[2*i+1][2*j+1] = "0"
        j += 1

    i += 1

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

    if tile == "S":
        poss = [(0,1),(0,-1),(1,0),(-1,0)]
    else:
        poss = pipeDirection[tile]
    i,j = current

    #! Part 2
    x0, y0 = current[0] * 2, current[1] * 2
    newMap[x0][y0] = tile
    # Clearing the offset for expanded map spaces where there shouldn't be a tile
    newMap[x0+1][y0+1] = " "
    

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
            previous = current
            return next, previous, tile
    print('crap')


previous = None
length = 0
current = start

tile = 'S'
next, previous, nextTile = findNext(lines, current, previous, tile)
pathing = []
pathing.append(current)

while nextTile != 'S':
    tile = nextTile
    current = next
    
    next, previous, nextTile = findNext(lines, current, previous, nextTile)
    pathing.append(current)
    
    #! Part 2
    x0, y0 = previous 
    x1, y1 = next
    length += 1

pathing.append(next)

print("P1 Answer: ",length/2)

# Part 2 Logic (thanks Robin)
isInside = 0
i = 0
while i < len(newMap):
    countFlats = 0
    j = 0
    while j < len(newMap[i]):
        if newMap[i][j] == "|":
            countFlats += 1
        if newMap[i][j] == "0":
            newMap[i-1][j-1] = "0"
            if countFlats % 2 == 1:
                isInside += 1

                #! everything below is just visualizing cleanup
                newMap[i-1][j-1] = "I"
            newMap[i][j] = " "

        if newMap[i][j] in "7JFL":
            newMap[i][j] = "*"
            
        j += 1
    i += 1
print("P2 Answer:",isInside)

# oldCount = 0
# for line in lines:
#     for x in line:
#         if x == ".":
#             oldCount += 1

# newCount = 0
# for line in newMap:
#     for x in line:
#         if x == "0":
#             newCount+=1

# print(oldCount, newCount)

#! Output Visual
# for line in newMap:
#     print(" ".join([x for x in line]))