import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())



theInput = open("Input").read()

lines = theInput.split("\n")

delimiter = ','
delim = theInput.split(delimiter)

#####
alph = 'abcdefghijklmnopqrstuvwxyz'

#####
parse = lines
#parse = lines
total = 0

rock = 1
paper = 2
sci = 3

win = 6
draw = 3
loss = 0

oR = 'A'
oP = 'B'
oS = 'C'

draw = 'Y'
lose = 'X'
win = 'Z'

winning = {oR: paper, oP: sci, oS: rock}
drawing = {oR: rock, oP: paper, oS: sci}
losing = {oR: sci, oP: rock, oS: paper}

total = 0
for p in parse:
    him, me = p.split(' ')

    if me == 'Y':
        total += drawing[him] + 3
    if me == 'X':
        total += losing[him] + 0
    if me == "Z":
        total += winning[him] + 6
    #if [him, me] in winning:
    #    total += 6
    
    #if [him, me] in drawing:
    #    total += 3

    

print(total)


    
    



