cases = int(input().rstrip())
data = [""] * cases

def key(input): return str(int(input == "BROKEN"))

def nBase(num, base):
    if num == 0: return ["0"]
    nums = []
    while num > 0:
        nums.append(str(num % base))
        num //= base
    return nums[::-1]

lights = ["off", "red", "green", "blue"]
for i in range(cases):
    statuses = ''.join(nBase(int(''.join(list(map(key, input().rstrip().split(" ")))), 2), 4)).zfill(2)
    string = ""
    for num in statuses: string += lights[int(num)] + " "
    data[i] = string.rstrip()

for i in range(cases): print(data[i])
