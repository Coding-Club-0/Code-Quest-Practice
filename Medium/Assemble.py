# Medium Problem
import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

def checkDifferences(arr):
    newArr = []
    for i in range(len(arr)):
        canAdd = True
        for j in range(len(arr)):
            if i != j: 
                if abs(arr[i] - arr[j]) >= 10:
                    canAdd = False
                    break
        if canAdd: newArr.append(i)
    return newArr

people = [0] * cases
values = [0] * cases
for i in range(cases):
    d = data[i].split(" ")
    people[i] = [0] * len(d)
    values[i] = [0] * len(d)

    for j in range(len(d)):
        c = d[j].split("=")
        people[i][j] = c[0]
        values[i][j] = int(c[1])
    print(values[i])

for i in range(cases):
    new = checkDifferences(values[i])
    string = ""
    for index in new:
        string += people[i][index] + " "
    print(string.strip())
    



