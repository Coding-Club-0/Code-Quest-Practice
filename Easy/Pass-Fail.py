cases = int(input().rstrip())
data = [0] * cases
for i in range(cases): data[i] = int(input().rstrip())
for i in range(cases):
    if data[i] >= 70: print("PASS")
    else: print("FAIL")