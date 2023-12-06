import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())



theInput = open("Input").read()

lines = theInput.split("\n\n")

delimiter = ','
delim = theInput.split(delimiter)

#####
alph = 'abcdefghijklmnopqrstuvwxyz'

#####
parse = lines
#parse = lines
total = 0
max1 = 0
arr = [0,0,0]
for p in parse:
    if not p:
        #if total > max(arr):
            #arr[0] = total
            #arr.sort()
        arr.append(total)
        total = 0
    else:
        total += int(p)

#print(arr)
arr.sort()
print(arr[-3:])

# AOC 2023 Day 1