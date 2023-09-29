cases = int(input().rstrip())

for case in range(cases):
    value = input().rstrip().split(" ")
    print(value.index("Nimo")+1)