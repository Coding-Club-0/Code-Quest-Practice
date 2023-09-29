import math
cases = int(input().rstrip())

for case in range(cases):
    data = list(map(float, input().rstrip().split(" ")))
    x1, y1, x2, y2, w, n = data

    wx = (x1 + x2) / 2 - w/2
    A = x1 - wx
    B = x2 - wx
    S = A+B
    for i in range(int(n)):
        x, y = list(map(float, input().rstrip().split(" ")))
        C = math.dist((x1, y1), (x, y))
        D = math.dist((x2, y2), (x, y))
        inEllipse = C + D <= S
        print(int(inEllipse))
    
            