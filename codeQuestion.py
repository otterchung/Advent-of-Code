input = "3,5,1,7,2,3,4,1"
input = "3,5,1,7,2,7,1,4,1"
input = "6,3,5,1,7,2,3,1,4,1,5"

intArr = [int(x) for x in input.split(",")]

i = 1
low = 0
high = 0
total = 0
while i < len(intArr) - 1:
    left = intArr[:i]
    right = intArr[i+1:]
    point = intArr[i]

    leftMax = max(left)
    rightMax = max(right)

    if point < leftMax and point < rightMax:
        total += min(leftMax, rightMax) - point

    i += 1
print(total)