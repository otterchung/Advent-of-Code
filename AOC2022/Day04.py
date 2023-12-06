import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())


theInput = open("SampleInput").read()
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
for p in parse:
    yes = False
    a, b = p.split(',')

    a_i = [int(x) for x in a.split('-')]
    b_i = [int(x) for x in b.split('-')]

    #if a_i[0] <= b_i[0] and a_i[1] >= b_i[1]:
    if a_i[0] <= b_i[0] and a_i[1] >= b_i[0]:
        yes = True

    if a_i[0] <= b_i[1] and a_i[1] >= b_i[1]:
        yes = True

    if b_i[0] <= a_i[1] and b_i[1] >= a_i[1]:
        yes = True

    if b_i[0] <= a_i[1] and b_i[1] >= a_i[1]:
        yes = True
    
    if yes:
        total += 1
print(total)



