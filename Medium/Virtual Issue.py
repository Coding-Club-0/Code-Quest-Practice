cases = int(input().rstrip())
from decimal import * 


def value(x1, y1, x2, y2):
    return y1 + (3 - x1) / (x2 - x1) * (y2 - y1)
    
data = [0] * cases
for i in range(cases):
    time1, time2, time3, quality = list(map(Decimal, input().rstrip().split(" ")))
    targetFrameTime = Decimal(1000)/Decimal(90)
    lowThresh = Decimal(0.70) * targetFrameTime
    extThresh = Decimal(0.85) * targetFrameTime
    hiThresh = Decimal(0.9) * targetFrameTime
    if time3 > hiThresh: quality -= 2
    elif time3 > extThresh: 
        first = value(Decimal(0), time1, Decimal(2), time3)
        second = value(Decimal(1), time2, Decimal(2), time3)
        v = max(first, second)
        if v > hiThresh: quality -= 2
    elif time1 < lowThresh and time2 < lowThresh and time3 < lowThresh: quality += 1
    data[i] = int(quality)

for i in range(cases): print(data[i])


