import sys
import math

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

for d in data:
    d = d.split(" ")
    for i in range(len(d)):
        d[i] = int(d[i])
    Cr, Cg, Cb, T, Fr, Fg, Fb, Br, Bg, Bb = d
    dist = math.sqrt((Fr - Cr)**2 + (Fg - Cg)**2 + (Fb - Cb)**2)
    if dist <= T: print(Br, Bg, Bb)
    else: print(Fr, Fg, Fb)