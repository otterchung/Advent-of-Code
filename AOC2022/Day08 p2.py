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


def treeCheck(x,y):
    poss = 1
    poss_arr = []
    tree = arr[x][y]

    i = y-1
    j = 0
    isGood = True
    while i >= 0 and isGood:
        if arr[x][i] >= tree:
            isGood = False
        i -= 1
        j += 1
    poss *= j
    poss_arr.append(j)

    i = x-1
    j = 0
    isGood = True
    while i >= 0 and isGood:
        if arr[i][y] >= tree:
            isGood = False
        i -= 1
        j += 1
    poss *= j
    poss_arr.append(j)

    #up
    i = x+1
    j = 0
    isGood = True
    while i < x_len and isGood:
        #print(i,y, arr[i][y])
        if arr[i][y] >= tree:
            isGood = False
        i += 1
        j += 1
    poss *= j
    poss_arr.append(j)

    # right
    i = y+1
    j = 0
    isGood = True
    while i < y_len and isGood:
        if arr[x][i] >= tree:
            isGood = False
        i += 1
        j += 1
    poss *= j
    poss_arr.append(j)

    available.append(poss)
    return poss_arr

    

available = []
x = 0
y = 0
while x < x_len :
    y = 0
    
    while y < y_len:
        treeCheck(x,y)
        y += 1
    x += 1
    
print(max(available))
#43200