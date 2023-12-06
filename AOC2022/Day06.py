import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())

#import methods

theFileName = "SampleInput"
theFileName = "Input"

theInput = open(theFileName).read()
#lines = theInput.split("\n")

# delimiter = ','
# delim = theInput.split(delimiter)

# #####
# parse = lines
# #parse = lines

# total = 0
# arr = []
# i = 0
# for line in parse:
#     reline = line
#     #if line == '':
#     #    break
#     if theFileName == "SampleInput":
#         print(line)
    
#     arr.append(reline)

# total = 0
# for line in arr:
    
#     if theFileName == "SampleInput":
#         print(line)
arr = [x for x in 'zdrr']
arr = [x for x in 'zdrrgvvntvtzzs']
#arr = [x for x in 'nppd']
pos = 14
for letter in theInput:
    arr = arr[1:] + [letter]
    pos += 1
    if len(set(arr)) == len(arr):
        print(pos)
        break


#print('\n\n\nAns:', total)
print('Using', theFileName)
print(arr)
