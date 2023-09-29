import sys
import math

def newRound(num):
    return "%.3f" % round(num, 3)

cases = int(sys.stdin.readline().rstrip())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def inArray(string, array):
    for i in range(len(array)):
        if array[i][0] == string:
            return i
    return False

data = [0] * cases
whitelist = set(alphabet)

for i in range(cases):
    data[i] = []
    lines = int(input().rstrip())

    string = []
    for j in range(lines):
        string.append(input().rstrip().split(" "))
    
    strings2 = []
    for j in range(len(string)):
        for k in range(len(string[j])):
            strings2.append(''.join(filter(whitelist.__contains__, string[j][k].upper())))

    for j in range(len(strings2)):
        for k in range(0, len(strings2[j])):
            substr = strings2[j][k:k+2].strip()
            if len(substr) < 2: continue
            result = inArray(substr, data[i])
            if str(result) == "False": data[i].append([substr, 1])
            else: data[i][result][1] += 1

    for j in range(len(strings2)):
        for k in range(0, len(strings2[j])):
            substr = strings2[j][k:k+3]
            if len(substr) < 3: continue
            result = inArray(substr, data[i])
            if not result: data[i].append([substr, 1])
            else: data[i][result][1] += 1

totals = [0] * cases
for i in range(cases):
    totals[i] = [0, 0]
    for j in range(len(data[i])):
        b = data[i][j]
        totals[i][len(b[0])-2] += b[1]

def key(arr):
    return arr[0]

for i in range(cases):
    data[i].sort()
    string = []
    for j in range(len(data[i])):
        b = data[i][j]
        result = 100*b[1]/totals[i][len(b[0])-2]
        if len(b[0]) == 3: string.append([b[0], result])
        else: print(b[0] + ": " + newRound(result) + "%")
    for j in range(len(string)):
        print(string[j][0] + ": " + newRound(string[j][1]) + "%")

