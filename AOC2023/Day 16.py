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

#paths = [[[0,-1],[0,1]]] # position and direction


startPaths = []
map = []
i = 0
for line in lines:
    map.append([x for x in line])

    startPaths.append([[i, len(line)],[0,-1]])
    startPaths.append([[i,-1],[0,1]])
    i +=  1

i = 0 
for m in map[0]:
    startPaths.append([[len(map), i], [-1,0]])
    startPaths.append([[-1, i], [1,0]])
    i += 1





def exists(coor):

    x, y = coor
    #print(x,y)
    if x > len(map) - 1 or x < 0:
        return False
    if y > len(map[x]) - 1 or y < 0:
        return False
    return True
    
def explore():

    while len(paths) > 0:
        
        path = paths.pop()
        visited.append(path)
        coor, dir = path
        nextCoor = [coor[0] + dir[0], coor[1] + dir[1]]
        nextx, nexty = nextCoor
        dirx, diry = dir
        #print(exists(nextCoor))
        if exists(nextCoor):
            node = map[nextx][nexty]
            nextDir = []
            if node == ".":
                nextDir.append(dir)
            elif node == "/":
                nextDir.append([-diry, -dirx])

            elif node == "\\":
                nextDir.append([diry, dirx])
            elif node == "-":
                if abs(diry) > 0:
                    nextDir.append(dir)
                else:
                    nextDir.append([0, dirx])
                    nextDir.append([0, -dirx])
            elif node == "|":
                if abs(diry) > 0:
                    nextDir.append([diry, 0])
                    nextDir.append([-diry, 0])
                else:
                    nextDir.append(dir)
            
            for next in nextDir:
                
                path = [nextCoor, next]
                if path not in visited:
                    paths.append(path)
    print("exited")

energy = []
for sp in startPaths:
    paths = []
    visited = []
    paths.append(sp)
    #print(paths)
    explore()
    #print(visited)
    coors = []

    for v in visited:
        coor = v[0]

        if coor not in coors:
            coors.append(coor)

    energy.append(len(coors) - 1)
    #print(visited)
    #print(coors)
    #print(energy)

#print(len(coors) - 1)
print(max(energy))
print("Part2:",sum(collect2), collect2)

# 8212 too high - answer: 7541
#print(line)
#print("\t".join([x for x in springs]))
