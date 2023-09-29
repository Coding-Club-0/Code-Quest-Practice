# Easy Problem
import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

for d in data:
     if (isFibonacci(int(d)) == True):
         print("TRUE")
     else:
         print("FALSE")