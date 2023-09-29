vowels = "aeiou"

import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())
    
for sentence in data:
    count = 0
    for i in range(len(vowels)): count += [*sentence].count(vowels[i])
    print(count)