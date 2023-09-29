cases = int(input().rstrip())

strings = [""] * cases
for i in range(cases):strings[i] = input().rstrip()[::-1]
for i in range(cases):print(strings[i])