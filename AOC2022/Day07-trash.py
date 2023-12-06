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
parse = lines
#parse = lines

total = 0
arr = []
i = 0
directory = dict()
curDir = '/'
space = dict()
directory['/'] = []
space['/'] = 0
isNextSpace = False
listing = False
isCommand = False

revDirectory = dict()
topDirectory = dict()
topDirectory['/'] = []
prevDir = ""
for p in parse:

    line = p.split(' ')

    if listing:
        if line[0] == '$':
            listing = False
        elif line[0] == 'dir':
            if line[1] in directory.keys():
                print('what', line[1])
            if line[1] not in directory.keys():
                directory[line[1]] = []
                topDirectory[line[1]] = []
            if line[1] not in space.keys():
                space[line[1]] = 0
            directory[curDir].append(line[1])

            revDirectory[line[1]] = curDir
            up = curDir
            # while up in revDirectory.keys():

            #     oneHigher = revDirectory[up]
            #     topDirectory[oneHigher].append(up)
            #     up = oneHigher

        else:
            space[curDir] += int(line[0])

    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                curDir = revDirectory[curDir]
            else:
                #prevDir = curDir
                curDir = line[2]
        elif line[1] == 'ls':
            listing = True


def check(key):
    total = 0

    print(key)
    if len(directory[key]) == 0:
        return space[key]
    else:
        for a in directory[key]:
            total += check(a)
    return 0

# respace = dict()
# newSpace = dict()
# for key in revDirectory.keys():
#     newSpace[key]
#     revDirectory[key] = newSpace[key]



# total = 0
# for key in respace.keys():
#     if respace[key] > 10000:
#         total += 1

print(total)
#118
print('Using', theFileName)