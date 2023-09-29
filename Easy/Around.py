import sys
import math

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

r = 40075 / (2 * math.pi)

for d in data:
    print(round(2 * math.pi * (r + float(d)), 1))