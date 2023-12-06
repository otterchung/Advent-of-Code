import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())


theInput = open("SampleInput").read()
#theInput = open("Input").read()

lines = theInput.split("\n")

delimiter = ','
delim = theInput.split(delimiter)

#####
alph = 'abcdefghijklmnopqrstuvwxyz'

#####
parse = lines
#parse = lines


# arr = []
# arr.append('ZN')
# arr.append('MCD')
# arr.append('P')

#         [G]         [D]     [Q]    
# [P]     [T]         [L] [M] [Z]    
# [Z] [Z] [C]         [Z] [G] [W]    
# [M] [B] [F]         [P] [C] [H] [N]
# [T] [S] [R]     [H] [W] [R] [L] [W]
# [R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
# [C] [N] [H] [R] [N] [H] [D] [J] [Q]
# [N] [D] [M] [G] [Z] [F] [W] [S] [S]

arr = []
arr.append('NCRTMZP')
arr.append('DNTSBZ')
arr.append('MHQRFCTG')
arr.append('GRZ')
arr.append('ZNRH')
arr.append('FHSWPZLD')
arr.append('WDZRCGM')
arr.append('SJFLHWZQ')
arr.append('SQPWN')


total = 0
for line in parse:
    move, num, fr, box1, to, box2 = line.split(' ')

    i = 0
    #while i < int(num):
    print(arr, box1, box2)
    #if len(arr[int(box1) - 1]) > 0 :
    moving = arr[int(box1) - 1][-int(num):]
    print(moving)
    arr[int(box1) - 1] = arr[int(box1) - 1][0:-int(num)] 
    arr[int(box2) - 1] += moving
    i += 1

let = ""
for a in arr:
    print(a[-1])
    let += a[-1]
print (let)
