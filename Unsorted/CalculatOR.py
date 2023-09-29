cases = int(input().rstrip())
import math

def roundUp(num):
    whole = int(num)
    decimal = 10*(num % 1)
    # if whole < 0:
        # return f'{whole}.{int(decimal)}'
    return f'{whole}.{math.ceil(decimal)}'

for case in range(cases):
    num1, operator, num2 = input().rstrip().split(" ")
    num1 = int(num1)
    num2 = int(num2)

    value0 = num1
    value1 = num2
    if operator == "+":
        value0 += num2
        value1 += num1
    elif operator == "-":
        value0 -= num2
        value1 -= num1
    elif operator == "*":
        value0 *= num2
        value1 *= num1
    elif operator == "/":
        value0 /= num2
        value1 /= num1
    
    print(f'{roundUp(value0)} {roundUp(value1)}')
4
1 + 2
2 - 3
3 * 4
4 / 5