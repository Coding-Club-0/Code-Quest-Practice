# Easy Problem
import math
import sys

def nthterm(n):
    if n == 1: return 0
    if n < 4: return 1
    num = 1
    prev = 1
    for term in range(n-3):
        temp = num
        num += prev
        prev = temp
    return num

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

for d in data:
    print(d + " = " + str(int(nthterm(int(d)))))
