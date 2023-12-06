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
for line in parse:
    reline = line
    #if line == '':
    #    break
    if theFileName == "SampleInput":
        print(line)
    
    arr.append(reline)

total = 0
for line in arr:
    
    if theFileName == "SampleInput":
        print(line)


print('\n\n\nAns:', total)
print('Using', theFileName)