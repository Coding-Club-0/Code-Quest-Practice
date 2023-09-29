import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

for d in data:
    d = d.split(" ")
    numer = 0
    den = 0
    try:
        numer = (float(d[0]))
    except:
        print("Invalid Dividend")
        continue

    try:
        den = (float(d[1]))
    except:
        print("Invalid Divisor")
        continue

    if den == 0:
        print ("Divide By Zero")
        continue
    a = "%.1f" % round(numer/den, 1)
    print(a)