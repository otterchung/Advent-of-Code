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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

coor = (0,0)

#length = 0
allx, ally = [], []

lengths = dict() # @ x, [y1 to y2]  | R/L | [ x:[y1, y2], ...]
ranges = [] # along x, y        | U/D | [ [x1, x2], y], ... ]

cc_iter = 0
c_iter = -1
turn = "__"
lengthTotals = 0
for line in lines:

    store = None


    # part 1
    direction, mag, color = line.split(" ")
    mag = int(mag)
    
    if not part1:
        # part 2
        color = color.strip("()")
        directionDict = {0: "R", 1: "D", 2: "L", 3: "U"}
        direction = directionDict[int(color[-1])]

        mag = int(color[1:-1], 16)
        
    # -----
    #print(coor)
    x, y = coor

    newx, newy = x,y

    if direction == "R":

        if x not in lengths:
            lengths[x] = []

        newy = y + int(mag)        
        lengths[x].append( [y, newy] )
    
    if direction == "L":

        if x not in lengths:
            lengths[x] = []

        newy = y - int(mag)        
        lengths[x].append( [newy, y] )

    if direction == "U":
        newx = x - int(mag)        
        ranges.append( [[newx, x], y] )

    if direction == "D":
        newx = x + int(mag)        
        ranges.append( [[x, newx], y] )

    lengthTotals += mag
    coor = (newx, newy)
    allx.append(newx)
    ally.append(newy)
    
#------

total_x = max(allx) - min(allx)
offset_x = -min(allx)

total_y = max(ally) - min(ally)
offset_y = -min(ally)

ranges.sort()

r = 0
l = 0

totalArea = []
#print(min(allx), max(allx), ":", total_x, total_y, total_x*total_y)
for x in range( min(allx), max(allx) ):
    arr = []
    #! get length y (counts as one point)
    if x in lengths.keys():
        # for z in lengths[x]:
        #    arr += z
        arr += lengths[x]

        # do add

    #! get ranges y
    sides = 0
    for xs, y in ranges:
        if x > xs[0] and x < xs[1]:
            # arr += [y]
            arr.append([y])
            sides += 1
    
    # lineArea = 0
    # i = 0
    # while i < len(arr):
    #     if len(arr[i]) == 1 and len(arr[2])

    arr.sort()

    if x % 1000000 == 0:
        print( int( x / 1000000) )
    #print(x, arr)
    openVal = None
    area = 0
    for a in arr:

        if openVal != None:
            area += min(a) - openVal - 1
            openVal = None
        else:
            openVal = max(a)
    totalArea.append(area)
    #print("Line Area:", area)

print(sum(totalArea), lengthTotals)
print(sum(totalArea) +  lengthTotals)

    



# too high: 389147726391322
# still high: 309147726391322

# too low: 109147726391322, 1E14

# not 209147726391322
# not 250021895803864



# p2 sample:    
#   952407934574 mine (a little less)
#   952408144115 theirs

# p1 actual:
#       answer
#       mine

# p2 actual:
#       250021895803864 mine (a little less?)