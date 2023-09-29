import math

cases = int(input().rstrip())
nums = ["LOW", "MEDIUM", "HIGH"]

def realRound(num):
    if num % 1 >= 0.5:
        return math.ceil(num)
    return math.floor(num)

for case in range(cases):
    values = int(input().rstrip())

    s = 0
    for value in range(values):
        priority, multiplier = input().rstrip().split(" ")
        m = nums.index(priority)+1
        values += nums.index(priority)
        s += m * int(multiplier)
    
    print(realRound(s/values*10))