import os

if "Files/Random Codes/AOC2023" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
data = "actual"

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "SampleInput.txt"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "Input.txt"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print(lines[0])

total = 0
finalString = ""
collect = []

numline = "123456789"
newnum = "one,two,three,four,five,six,seven,eight,nine,ten"

numArr = newnum.split(",")
for line in lines:
    i = 0
    # for num in numArr:
    #     line = line.replace(num, str(i))
    #     i += 1
    first = ""
    second = ""
    letters = []
    for a in line:
        
        if a in numline:
            first = a
            break
        
        i = 0
        while i < len(letters):
            letters[i] += a

            if  letters[i] in numArr:
                #print('yes')
                first = str(1+numArr.index(letters[i]))
                break
            i += 1

        letters.append(a)

        if len(first) > 0:
            break
    #print(letters)
    #print(first)

    rline = [x for x in line]
    rline.reverse()

    letters = []
    for a in rline:
        #print(a)
        if a in numline:
            second = a
        
        i = 0
        while i < len(letters):
            letters[i] = a + letters[i]
            #print(letters)
            if  letters[i] in numArr:
                #print('yes')
                second = str(1+numArr.index(letters[i]))
            i += 1

        letters.append(a)
        #print(letters)
        if len(second) > 0:
            break

    print("hello" + first + second)
        
    #print(newline)
    #print(newline[0] + newline[-1])
    total = int(first + second)


    collect.append(total)
    #print(line)
print(collect)
print(sum(collect))
#print(collect)
# 46255
# collect.sort()
# collect.reverse()
# print(collect[:3])