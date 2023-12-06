import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())

import methods

theFileName = "SampleInput.txt"
#theFileName = "Input.txt"

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
head = [0,0]
tail = [0,0]
map_of_tails = [[0,0]]
for line in parse:
    direction, moves_h = line.split(' ')
    moves = int(moves_h)
    i = 0
    print('----', direction, moves)
    while i < moves:
        
        if direction == "R":
            head = [head[0] + 1, head[1]]
            
            if head[0] != tail[0]:
                if head[0] - tail[0] > 1:
                    tail = [head[0]-1, head[1]]
                else:
                    tail = [head[0]-1, tail[1]]


        if direction == "U":
            head = [head[0], head[1] + 1]

            if head[1] != tail[1]:
                if head[1] - tail[1] > 1:
                    tail = [head[0], head[1]-1]
                else:
                    tail = [tail[0], head[1]-1]

        if direction == "L":
            head = [head[0] - 1, head[1]]
            if head[0] != tail[0]:
                if abs(head[0] - tail[0]) > 1:
                    tail = [head[0]+1, head[1]]
                else:
                    tail = [head[0]+1, tail[1]]

        if direction == "D":
            head = [head[0], head[1] - 1]
            if head[1] != tail[1]:
                if abs(head[1] - tail[1]) > 1:
                    tail = [head[0], head[1]+1]
                else:
                    tail = [tail[0], head[1]+1]
        i += 1 

        map_of_tails.append(tail)
        print('h: ',head)
        print('t: ',tail)

str_map = ['.'.join(str(x)) for x in map_of_tails]

print(len(set(str_map)))
#3739