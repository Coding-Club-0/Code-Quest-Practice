cases = int(input().rstrip())

data = [0] * cases
for i in range(cases):
    num = int(input().rstrip())
    original = num
    count = 0
    while num > 1:
        if num % 2 == 0: num //= 2
        else: num = 3 * num + 1
        count += 1
    data[i] = f'{original}:{count+1}'

for i in range(cases): print(data[i])