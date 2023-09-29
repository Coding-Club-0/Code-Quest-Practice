alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def indexOf(str, arr):
    for i in range(len(arr)):
        if arr[i] == str:
            return alphabet[i]
    return "0"

import sys

cases = int(sys.stdin.readline().rstrip())
data = [0] * cases
for i in range(cases):
    data[i] = [0] * 3
    a1 = [0] * 26
    for j in range(26):
        a = input().rstrip()
        a = a.split(" ")
        a.pop(0)
        a1[j] = ' '.join(a)

    data[i][0] = a1
    data[i][1] = input().rstrip()
    b = input().rstrip().split("       ")
    c = [0] * len(b)
    for j in range(len(b)):
        c[j] = b[j].split("  ")

    data[i][2] = c

# def concat(array):
#     newArr = []
#     for i in range(len(array)):
#         for j in range(len(array[i]))
#             newArr.append(array)

for i in range(cases):
    string = ""
    for j in range(len(data[i][1])):
        try:
            b = data[i][1][j]
            string += data[i][0][alphabet.index(b)] + "   "
        except:
            string += "    "
            continue
    print(string.strip())

    string = ""
    for j in range(len(data[i][2])):
        for k in range(len(data[i][2][j])):
            b = data[i][2][j][k].strip()
            string += indexOf(b, data[i][0])
        string += " "
    print(string.strip())
   
