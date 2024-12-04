import os

if not 'AOC2024/inputs' in os.getcwd():
    os.chdir('/Users/ahuang/Documents/Work/alan_github/Advent-of-Code/AOC2024/inputs')

newInputFile = open("4-input")
newInput = newInputFile.read()
newInputFile.close()

# Sample Input
yourInput = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# Given Input
yourInput = newInput
array = []
for line in yourInput.split("\n"):
    array.append([x for x in line])

# Part 2
def exploreMas(x,y):
    set1 = getletter(x+1,y+1) + getletter(x-1,y-1)
    set2 = getletter(x+1,y-1) + getletter(x-1,y+1)

    if (set1 in ("MS", "SM")) and (set2 in ("MS", "SM")):
        return 1
    return 0

def getletter(x,y):
    if x >= len(array[0]) or x < 0:
        return "R"
    if y >= len(array) or y < 0:
        return "R"
    #print(y,x,array[y][x])
    return array[y][x]

# Part 1 
def explore(x,y):
    term = 'MAS'
    right = True
    left = True
    up = True
    down = True
    upleft = True
    upright = True
    downleft = True
    downright = True
    j = 1
    for i in term:
        # right
        if right:
            newx = x + j
            newy = y
            right = check(newx,newy,i)
        
        # left
        if left:
            newx = x - j
            newy = y
            left = check(newx,newy,i)

        # up
        if up:
            newy = y + j
            newx = x
            up = check(newx,newy,i)

        # down
        if down:
            newy = y - j
            newx = x
            down = check(newx,newy,i)

        # upleft
        if upleft:
            newy = y + j
            newx = x - j
            upleft = check(newx,newy,i)

        # upright
        if upright:
            newy = y + j
            newx = x + j
            upright = check(newx,newy,i)

        # downright
        if downright:
            newy = y - j
            newx = x + j
            downright = check(newx,newy,i)

        # downleft
        if downleft:
            newy = y - j
            newx = x - j
            downleft = check(newx,newy,i)
        j += 1
       
    return up + down + left + right + downleft + downright + upleft + upright

def check(x,y,i):
    if x >= len(array[0]) or x < 0:
        return False
    if y >= len(array) or y < 0:
        return False
    if array[y][x] != i:
        return False
    return True

total = 0
total2 = 0
for i in range(0,len(array)): #y
    line = array[i]
    for j in range(0,len(line)): #x
        if array[j][i] == "X":
            total += explore(i,j)
        if array[j][i] == "A":
            total2 += exploreMas(i,j)


print(total, total2)