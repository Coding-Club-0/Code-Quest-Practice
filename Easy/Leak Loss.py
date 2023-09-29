from decimal import *
import math
cases = int(input().rstrip())

def roundToNearest(num):
    if num % 1 >= 0.5: return math.ceil(num)
    else: return math.floor(num)

def leaked_water(pool_volume, fill_rate, leak_rate):
    return leak_rate * pool_volume / (fill_rate - leak_rate)

data = [0] * cases
for i in range(cases):
    volume, fill, leak = list(map(float, input().rstrip().split(" ")))
    data[i] = leaked_water(volume, fill, leak)

for i in range(cases):
    print(roundToNearest(data[i]))