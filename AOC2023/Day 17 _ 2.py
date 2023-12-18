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


largeVal = 1000
map = []
for line in lines:
    map.append([largeVal] + [int(x) for x in line] + [largeVal])

map  = [[largeVal] * len(map[0])] + map + [[largeVal] * len(map[0])]

start = (1,1) # node, value
endNode = (len(map) - 2, len(map[-2]) - 2)
valDict = dict() # value: [path]
#! value -> node -> bestValPath
def possibleDir(path):
    node, value, direction, sameAdd = path
    maxSame = 2

    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    for d in directions:
        nextAdd = 0
        if d == direction:
            nextAdd = sameAdd + 1
            if nextAdd > maxSame:
                continue

        nextNode = (node[0] + d[0], node[1] + d[1])
        nextNodeVal = map[nextNode[0]][nextNode[1]] + value
        nextPath = nextNode, nextNodeVal, d, nextAdd

        if nextNodeVal not in valDict.keys():
            #valDict[nextNodeVal] = [] #!
            valDict[nextNodeVal] = dict()

        # if (nextNode[0], nextNode[1]) not in explored: 
        #     valDict[nextNodeVal].append(nextPath) 

        if nextNode in valDict[nextNodeVal]:
            # do comparison
            compNode, compValue, compDirection, compAdd = valDict[nextNodeVal][nextNode]
            if compValue < nextNodeVal or compAdd < nextAdd:
                valDict[nextNodeVal][nextNode] = nextPath

        else:
            valDict[nextNodeVal][nextNode] = nextPath

        


        


explored = set()

possibleEnds = []
def explore(map, start, endNode):
    # node, value, direction, sameAdd = path
    initialPath = start, 0, [-100, -100], 0
    possibleDir(initialPath)

    i = 0

    bestPath = None
    # get the smallest value in valDict: value -> node -> path
    notFound = True
    while notFound:
        if i in valDict.keys():
            nextNodes = valDict[i]
            for node in nextNodes.keys():
                path = nextNodes[node]
                #print(path)
                node, value, direction, sameAdd = path
                if node == endNode:
                    possibleEnds.append(path)
                    bestPath = value
                
                if bestPath != None and i > bestPath:
                    return possibleEnds
                
                #explored.add((node[0], node[1]))
                possibleDir(path)

            print(i, len(valDict[i]), len(explored))
        i += 1

hello = explore(map, start, endNode)

print(hello)
