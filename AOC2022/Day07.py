import os
import sys

#sys.setrecursionlimit(100000)

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())

import methods

theFileName = "SampleInput"
theFileName = "Input"

theInput = open(theFileName).read()
lines = theInput.split("\n")

delimiter = ','
delim = theInput.split(delimiter)

#####
listing = False
parse = lines
path = []
pathDict = dict()
pathDict['/'] = 0
pathDictPoss = dict()
for p in parse:
    line = p.split(' ')

    if listing:
        if line[0] == '$':
            listing = False

        elif line[0] == 'dir':
            pathDict['-'.join(path + [line[1]])] = 0
        else:
            pathFollow = []
            for x in path:
                pathFollow.append(x)
                pathDict['-'.join(pathFollow)] += int(line[0])
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                path.pop()
            else:
                path.append(line[2])
        elif line[1] == 'ls':
            listing = True




print(total)

currently = 43562874
actualDisc = 70000000 - currently

poss = []
for x in pathDict.keys():
    if actualDisc + pathDict[x] > 30000000:
        poss.append(pathDict[x])
print(min(poss))