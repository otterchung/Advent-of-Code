import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
data = "actual"
part1 = True #True

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
dig = dict() # x -> [y1, y2, y3]
for line in lines:

    # part 1
    direction, mag, color = line.split(" ")

    # part 2
    color = color.strip("()")
    #directionDict = {0: "R", 1: "D", 2: "L", 3: "U"}
    #direction = directionDict[int(color[-1])]

    # mag = int(color[1:-1], 16)


    #print(coor)
    x, y = coor

    newx, newy = x,y

    if x not in dig.keys():
        dig[x] = []

    if direction == "R":
        for i in range(1,int(mag)+ 1):
            dig[x].append(y + i)
        newy = y + int(mag)
        

    if direction == "L":
        for i in range(1,int(mag)+ 1):
            dig[x].append(y - i)
        newy = y - int(mag)

    if direction == "U":
        for i in range(1,int(mag)+ 1):

            if x-i not in dig.keys():
                dig[x-i] = []

            dig[x - i].append(y)
        newx = x - int(mag)
    if direction == "D":
        for i in range(1,int(mag)+ 1):
            if x+i not in dig.keys():
                dig[x+i] = []
                
            dig[x + i].append(y)
        newx = x + int(mag)

    coor = (newx, newy)
    
    
total = []
for x, ys in dig.items():
    #print(x)
    total.append(max(ys) - min(ys) + 1)
print("Ans:", sum(total), total)

# too high 257968

# too high 96684

#---- get map ----
total_x = max(dig.keys()) - min(dig.keys())
offset_x = -min(dig.keys())

max_y = 0
min_y = 100
for ys in dig.values():

    if min(ys) < min_y:
        min_y = min(ys)

    if max(ys) > max_y:
        max_y = max(ys)

total_y = max_y - min_y
offset_y = -min_y

map = []
for x in range(0, total_x + 1 + 2):
    map.append(["."] * (total_y + 1 + 2))

for x,ys in dig.items():
    for y in ys:
        map[x + offset_x + 1][y + offset_y + 1] = "#"

for m in map:
    print(" ".join(m))

start = (0,0)

nodes = set()

explore = [start]

while len(explore) > 0:

    nextNode = explore.pop()

    x, y = nextNode

    for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        newx, newy = x+dx, y+dy
        if newx >= 0 and newx <= len(map)-1 and newy >= 0 and newy <= len(map[0]) - 1:
            
            if map[newx][newy] == ".":

                if (newx,newy) not in nodes:
                    explore.append([newx,newy])
                nodes.add((newx,newy))

# ans: 76387

answer = len(map) * len(map[0]) - len(nodes)





