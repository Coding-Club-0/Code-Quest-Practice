import sys
import math

cases = int(sys.stdin.readline().rstrip())

data = [0] * cases

for i in range(cases):
    num = int(input().rstrip())
    data[i] = [0] * num

    for j in range(num):
        data[i][j] = ["", "", 0, 0]
        d = input().rstrip().split(":")
        b = d[0].split("_")
        c = d[1].split(",")
        data[i][j][0] = b[0]
        data[i][j][1] = b[1]
        data[i][j][2] = int(c[0])
        data[i][j][3] = int(c[1])

def getDistX(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append([arr[i][2], arr[i][3]])
    return newArr

def getMinIndex(arr):
    minValue = arr[0][0]
    minIndex = 0

    for i in range(1, len(arr)):
        if arr[i][0] < minValue:
            minValue = arr[i][0]
            minIndex = i
    
    yValues = []
    for i in range(0, len(arr)):
        if arr[i][0] == minValue:
            yValues.append(i)

    if len(yValues) > 1:
        maxValue = arr[yValues[0]][1]
        maxIndex = yValues[0]

        for i in range(1, len(yValues)):
            if arr[yValues[i]][1] > maxValue:
                maxValue = arr[yValues[i]][1]
                maxIndex = yValues[i]

        minIndex = maxIndex

    return minIndex
    

for i in range(cases):
    while len(data[i]) > 0:
        distances = getDistX(data[i])
        destroyIndex = getMinIndex(distances)

        print("Destroyed Ship: " + data[i][destroyIndex][0] + " xLoc: " + str(data[i][destroyIndex][2]))
        data[i].pop(destroyIndex)
        for j in range(len(data[i])):
            ship = data[i][j]
            if   ship[1] == "A": ship[2] -= 10
            elif ship[1] == "B": ship[2] -= 20
            elif ship[1] == "C": ship[2] -= 30