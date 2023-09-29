import sys
cases = int(sys.stdin.readline().rstrip())
data = [""] * cases

for i in range(cases):
    current = sys.stdin.readline().rstrip().rstrip()
    current = current.split(":")
    data[i] = current

for i in range(cases):
    v = float(data[i][0])
    d = float(data[i][1])

    if v == 0: 
        print("SAFE")
        continue

    t = d/v
    
    if t <= 1: print("SWERVE")
    elif t <= 5: print("BRAKE")
    else: print("SAFE")
