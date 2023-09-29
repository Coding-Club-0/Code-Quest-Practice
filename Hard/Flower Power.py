zero = [
        [' ', ' ', ' '],
        [' ', '*', ' '],
        [' ', ' ', ' '],
        ]

one = [
        ['\\', ' ', ' '],
        [' ', '*', ' '],
        [' ', ' ', ' '],
        ]

two = [
        ['\\', '|', ' '],
        [' ', '*', ' '],
        [' ', ' ', ' '],
        ]

three = [
        ['\\', '|', '/'],
        [' ', '*', ' '],
        [' ', ' ', ' '],
        ]

four = [
        ['\\', '|', '/'],
        [' ', '*', '-'],
        [' ', ' ', ' '],
        ]

five = [
        ['\\', '|', '/'],
        [' ', '*', '-'],
        [' ', ' ', '\\'],
        ]

six = [
        ['\\', '|', '/'],
        [' ', '*', '-'],
        [' ', '|', '\\'],
        ]

seven = [
        ['\\', '|', '/'],
        [' ', '*', '-'],
        ['/', '|', '\\'],
        ]

eight = [
        ['\\', '|', '/'],
        ['-', '*', '-'],
        ['/', '|', '\\'],
        ]

pedals = [zero, one, two, three, four, five, six, seven, eight]

def nBase(num, base):
    if num == 0: return [0]
    nums = []
    while num > 0:
        nums.append(num % base)
        num //= base
    return nums[::-1]

cases = int(input().rstrip())
data = [''] * cases
for i in range(cases):
    num = int(input().rstrip())
    base9 = nBase(num, 9)
    rows = [''] * 3
    for j in range(len(base9)):
        pedal = pedals[base9[j]]
        for k in range(3):
            rows[k] += ''.join(pedal[k]) + " "
    for j in range(3): rows[j] = rows[j].rstrip()
    data[i] = '\n'.join(rows)
for i in range(cases): print(data[i])

