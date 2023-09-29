import math

cases = int(input().rstrip())

def f(x):
    if x == 0:
        return 0
    
    return math.sin(x)/x 

def euler(x, y, h, num, depth):
    num += 1
    if num <= depth:
        y += h*f(x)
        x += h
        return euler(x, y, h, num, depth)
    else:
        return y
    
for case in range(cases):
    x, y, h, depth = map(float, input().rstrip().split(' '))
    print('%.3f' % round(euler(x, y, h, 0, int(depth)), 3))