cases = int(input().rstrip())

strings = [""] * cases
for i in range(cases):
    strings[i] = input().rstrip()

for i in range(cases):
    for j in range(2):
        print(strings[i])