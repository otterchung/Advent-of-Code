import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())

import methods

theFileName = "SampleInput.txt"
theFileName = "Input.txt"

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
map_of_tails = [[0,0]]

def moving(head, tail):

    if abs(head[1] - tail[1]) > 1 and abs(head[0] - tail[0]) > 1:
        tail[1] += int((head[1] - tail[1])/2)
        tail[0] += int((head[0] - tail[0])/2)
    if abs(head[1] - tail[1]) > 1:
        tail[1] += int((head[1] - tail[1])/2)
        if tail[0] != head[0]:
            tail[0] = head[0]
    
    
    elif abs(head[0] - tail[0]) > 1:
        tail[0] += int((head[0] - tail[0])/2)
        if tail[1] != head[1]:
            tail[1] = head[1]

    return tail

def moving_head(direction, head):
    if direction == "R":
        head = [head[0] + 1, head[1]]

    if direction == "U":
        head = [head[0], head[1] + 1]

    if direction == "L":
        head = [head[0] - 1, head[1]]

    if direction == "D":
        head = [head[0], head[1] - 1]
    return head    

knot = [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ]

for line in parse:
    direction, moves_h = line.split(' ')
    moves = int(moves_h)
    i = 0
    print('----', direction, moves)
    while i < moves:
        knot[0] = moving_head(direction, knot[0])

        #holder = knot[0]
        j = 1
        doNext = True
        while j < len(knot) :
            #head, tail
            knot[j] = moving(knot[j-1], knot[j])
            j += 1
        i += 1 

        print(knot)
        map_of_tails.append(knot[9].copy())


str_map = ['.'.join(str(x)) for x in map_of_tails]

print(len(set(str_map)))
#3739