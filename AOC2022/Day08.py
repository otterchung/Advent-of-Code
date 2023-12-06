import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())

import methods

theFileName = "SampleInput"

theInput = """30373
25512
65332
33549
35390"""

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
for line in parse:
    arr.append([int(x) for x in line])

x_len = len(line)
y_len = len(arr)

available = []
x = 0
y = 0
while x < x_len :
    y = 0
    while y < y_len:

        tree = arr[x][y]

        #moving y from 0 to ?
        i = 0
        isGood = True
        while i < y and isGood:
            if arr[x][i] >= tree:
                isGood = False
            i += 1
        if isGood:
            
            available.append((x,y))

        i = y+1
        isGood = True
        while i < y_len and isGood:
            if arr[x][i] >= tree:
                isGood = False
            i += 1
        if isGood:
            #print(x,y, tree)
            available.append((x,y))

        i = x+1
        isGood = True
        while i < x_len and isGood:
            if arr[i][y] >= tree:
                isGood = False
            i += 1
        if isGood:
            
            available.append((x,y))

        i = 0
        isGood = True
        while i < x and isGood:
            if arr[i][y] >= tree:
                isGood = False
            i += 1
        if isGood:
            print(x,y,tree)
            available.append((x,y))


        y += 1
    x += 1 

print(len(set(available)))
#4568
#2833