import math
cases = int(input().rstrip())
data = [0] * cases
R = 637e4

def degToRad(angle):
    return math.pi * angle / 180

for i in range(cases):
    theta = float(input().rstrip())
    data[i] = int(2 * math.cos(degToRad(theta)) * math.pi * R / 86400)

for i in range(cases): print(data[i])