import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())

import methods

theFileName = "SampleInput"
theFileName = "Input"

theInput = open(theFileName).read()
lines = theInput.split("\n")

secondInput = "Input2"
secondFile = open(secondInput).read().split('\n')

delimiter = ','
delim = theInput.split(delimiter)

#####
parse = lines
#parse = lines

arr = []
for line in parse:
    if line == '':
        break
    arr.append([x for x in line])

lastline = arr.pop()

initStackRead = []
for line in arr:
    boxes = []
    i = 0
    while i < len(lastline):
        if lastline[i] != ' ':
            boxes.append(line[i])
        i += 1
    initStackRead.append(boxes)

initStackRead = methods.matrixRotate(initStackRead, 1)

stack = []
for arr in initStackRead:
    stack.append([x for x in arr if x != ' '])
methods.printMatrix(stack)

for line in secondFile:
    move, num, fr, box1, to, box2 = line.split(' ')
    b1 = int(box1) - 1
    b2 = int(box2) - 1
    iters = int(num)

    tempStack = []
    for i in range(0,iters):
        tempStack.append(stack[b1].pop())
        #stack[b2].append(stack[b1].pop())
    
    tempStack.reverse()
    stack[b2] += tempStack

letters = ""
for s in stack:
    letters += s[-1]

print('\n\nAns',letters)

print('\nUsing', theFileName)