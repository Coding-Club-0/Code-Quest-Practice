# Medium Problem
import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

def euclids(n1, n2):
    a = max(n1 ,n2)
    b = min(n1, n2)

    gcd = 0
    while True:
        c = a - b
        print(str(a) + "-" + str(b) + "=" + str(c))

        if c == 0:
            gcd = b
            break

        a = max(b, c)
        b = min(b, c)

    if gcd == 1: print("COPRIME")
    else: print("NOT COPRIME")


for d in data:
    d = d.split(",")
    num1 = int(d[0])
    num2 = int(d[1])

    euclids(num1, num2)

