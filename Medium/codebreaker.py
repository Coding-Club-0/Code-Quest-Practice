import sys
import math

def newRound(num):
    return "%.2f" % round(num, 2)

cases = int(sys.stdin.readline().rstrip())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

data = [0] * cases
for i in range(cases):
    data[i] = [0] * 26
    lines = int(input().rstrip())

    string = ""
    for j in range(lines):
        string += input().rstrip()
    
    for letter in string:
        letter = letter.upper()
        if letter in alphabet:
            data[i][alphabet.index(letter)] += 1

def sum(list):
    count = 0
    for i in range(len(list)):
        count += list[i]
    return count

for i in range(len(data)):
    total = sum(data[i])
    for j in range(len(data[i])):
        result = 100*data[i][j]/total
        print(alphabet[j] + ": " + newRound(result) + "%")




