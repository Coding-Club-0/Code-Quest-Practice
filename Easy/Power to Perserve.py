cases = int(input().rstrip())
data = [0] * cases

import math
from decimal import *

for i in range(cases):
    diameter, revolutions, power, speed, capacity, voltage, distance = list(map(Decimal, input().rstrip().split(" ")))
    if voltage == 0 or speed == 0 or diameter == 0: 
        data[i] = "Fail"
        continue
    C = Decimal(math.pi) * diameter
    rotations = Decimal(100) * distance / C
    revMotor = rotations * revolutions
    time = revMotor / speed
    motorPower = revMotor * power
    totalCurrent = motorPower / voltage
    requiredCapcity = totalCurrent * time / Decimal(60)
    if capacity >= requiredCapcity: data[i] = f"Success {'%.4f' % round(time, 4)}"
    else: data[i] = "Fail"

for i in range(cases): print(data[i])