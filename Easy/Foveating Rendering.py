import math
cases = int(input().rstrip())

def insideRect(x0, y0, x, y, w, h):
    return x0 >= x and x0 <= x + w and y0 >= y and y0 <= y + h
 
def changeStrengths(x, y, arr):
    nums = [100, 90, 80]
    for i in range(-2, 3):
        for j in range(-2, 3):
            if insideRect(x+i, y+j, 0, 0, 19, 19):
                dist = math.isqrt(i ** 2 + j ** 2)
                arr[x+i][y+j] = nums[dist]

def printArray(arr):
    for i in range(len(arr)):
        string = ""
        for j in range(len(arr[i])):
            string += str(arr[i][j]) + " "
        print(string.rstrip())

data = [''] * cases
for i in range(cases):
    row, col = map(int, input().rstrip().split(" "))
    data[i] = [''] * 20
    for j in range(20): data[i][j] = [10] * 20
    changeStrengths(row, col, data[i])

for i in range(cases):
    printArray(data[i])
