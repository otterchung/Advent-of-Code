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
total = 0

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# total = 0
# for p in parse:
#     first = p[0:int(len(p)/2)]
#     second = p[int(len(p)/2):]
#     share = []
#     for letter in first:
#         if letter in second:
#             share.append(letter)
#     for letter in set(share):
#         total += alph.find(letter) + 1


# print(total)
#7262

total = 0
i = 0
share = []
while i < len(parse):
    first = parse[i]
    second = parse[i + 1]
    third = parse[i + 2]

    for x in first:
        if x in second:
            if x in third:
                share.append(x)
                break
    
    i += 3

total = 0
for letter in share:
    total += alph.find(letter) + 1
print(total)