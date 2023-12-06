def hello():
    print('world')

def matrixRotate_h(arr):
    newArr = []

    rowLen = len(arr[0])
    colLen = len(arr)

    for i in range(0,rowLen):
        line = []
        for j in range(0,colLen):
            line.append(' ')
        newArr.append(line)
    for i in range(0,rowLen):
        for j in range(0,colLen):
            cell = arr[colLen-1 - j][i]
            newArr[i][j] = cell
    return newArr

def matrixRotate(arr, iters):
    newArr = arr.copy()
    i = 0

    iters = iters % 4

    while i < iters:
        newArr = matrixRotate_h(newArr)
        i += 1
    return newArr

def matrixFlip_h(arr):
    newArr = []

    for line in arr:
        lineCopy = line.copy()
        lineCopy.reverse()
        newArr.append(lineCopy)
        
    return newArr

def matrixFlip_v(arr):
    return matrixRotate(matrixFlip_h(matrixRotate(arr,1)),-1)

def printMatrix(arr):
    for line in arr:
        print(line)

sampleArr = [[1,2], [3,4], [5,6]]

