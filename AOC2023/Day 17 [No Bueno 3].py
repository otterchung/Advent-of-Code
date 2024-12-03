import os

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

#paths = [[[0,-1],[0,1]]] # position and direction


largeVal = 10000
startInt = 10
map = []
for line in lines:
    map.append([largeVal]*startInt + [int(x) for x in line] + [largeVal]*startInt)

map  = [[largeVal] * len(map[0])]*startInt + map + [[largeVal] * len(map[0])]*startInt

start = (startInt,startInt) # node, value
endNode = (len(map) - startInt - 1, len(map[-startInt-1]) - startInt - 1)
valDict = dict() # value: [path]
#! value -> node -> bestValPath
def possibleDir(path):
    node, value, direction, sameAdd = path
    minDir = 4
    maxDir = 10

    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    for d in directions:
        nextAdd = 1
        if d == direction:
            #nextAdd = sameAdd + 1
            #if nextAdd > maxSame:
            continue
        
        # add up everything...
        valueAdd = 0
        if abs(d[0]) > 0:
            for i in [1,2,3,4,5,6,7,8,9,10]:
                valueAdd += map[node[0] + int(d[0] * i)][node[1]]

                if i >= 4:
                    nextNode = (node[0] + i, node[1])
                    nextNodeVal = map[nextNode[0]][nextNode[1]] + value + valueAdd
                    nextPath = nextNode, nextNodeVal, d, nextAdd

                    if nextNodeVal not in valDict.keys():
                        valDict[nextNodeVal] = dict()

                    if (nextNode[0], nextNode[1], i, d[1], sameAdd) in explored:
                        continue

                    if nextNode in valDict[nextNodeVal]:
                        # do comparison
                        for compPath in valDict[nextNodeVal][nextNode]:
                            compNode, compValue, compDirection, compAdd = compPath
                            
                            #if compPath != nextPath:
                                #if compValue > nextNodeVal and compAdd > nextAdd:
                                #    valDict[nextNodeVal][nextNode] = [nextPath]
                                
                            if nextPath not in valDict[nextNodeVal][nextNode]:
                            #and not (compValue > nextNodeVal and compAdd > nextAdd):
                                valDict[nextNodeVal][nextNode].append(nextPath)
                                #elif compValue == nextNodeVal:
                                #    valDict[nextNodeVal][nextNode].append(nextPath)

                    else:
                        valDict[nextNodeVal][nextNode] = [nextPath]
        else:
            for i in [1,2,3]:
                valueAdd += map[node[0]][node[1] + int(d[1] * i)]

                if i >= 4:
                    nextNode = (node[0], node[1] + i)
                    nextNodeVal = map[nextNode[0]][nextNode[1]] + value + valueAdd
                    nextPath = nextNode, nextNodeVal, d, nextAdd

                    if nextNodeVal not in valDict.keys():
                        #valDict[nextNodeVal] = [] #!
                        valDict[nextNodeVal] = dict()

                    # if (nextNode[0], nextNode[1]) not in explored: 
                    #     valDict[nextNodeVal].append(nextPath) 
                    if (nextNode[0], nextNode[1], d[0], i, sameAdd) in explored:
                        continue

                    if nextNode in valDict[nextNodeVal]:
                        # do comparison
                        for compPath in valDict[nextNodeVal][nextNode]:
                            compNode, compValue, compDirection, compAdd = compPath
                            
                            #if compPath != nextPath:
                                #if compValue > nextNodeVal and compAdd > nextAdd:
                                #    valDict[nextNodeVal][nextNode] = [nextPath]
                                
                            if nextPath not in valDict[nextNodeVal][nextNode]:
                            #and not (compValue > nextNodeVal and compAdd > nextAdd):
                                valDict[nextNodeVal][nextNode].append(nextPath)
                                #elif compValue == nextNodeVal:
                                #    valDict[nextNodeVal][nextNode].append(nextPath)

                    else:
                        valDict[nextNodeVal][nextNode] = [nextPath]
        

       

        


        
#787 too low

#792 too high
#789 incorrect
#801 incorrect
#790 incorrect
#788 incorrect

# next: 791

# part 2
#low: 875
#high: 925

#next: 900




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
            nextNodes = valDict[i] #returns a node dictionary, each node has a [path]
            for node in nextNodes.keys():
                #path = nextNodes[node]
                for path in nextNodes[node]:
                #print(path)
                    node, value, direction, sameAdd = path
                    if node == endNode:
                        possibleEnds.append(path)
                        bestPath = value
                        print(bestPath)
                    
                    if bestPath != None and i > bestPath+2:
                        return possibleEnds
                    
                    
                    possibleDir(path)
                explored.add((node[0], node[1], direction[0], direction[1], sameAdd))

            print(i, len(valDict[i]), len(explored))
        i += 1

hello = explore(map, start, endNode)

print(hello)
for h in hello:
    print(h)