cases = int(input().rstrip())
data = [0] * cases
for i in range(cases): data[i] = input().rstrip().split(" ")
for i in range(cases):
    num = data[i][0]
    method = data[i][1]
    if method == "PARENTHESES": print(f'({num[0:3]}) {num[3:6]}-{num[6:]}')
    elif method == "DASHES": print(f'{num[0:3]}-{num[3:6]}-{num[6:]}')
    elif method == "PERIODS":print(f'{num[0:3]}.{num[3:6]}.{num[6:]}')
