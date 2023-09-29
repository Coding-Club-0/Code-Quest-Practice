cases= int(input().rstrip())

data = [""] * cases
for i in range(cases):
    d = input().rstrip().split(" ")
    bday = d[1] == "true"
    speed = int(d[0]) - 5*int(bday)
    if speed <= 60: data[i] = "no ticket"
    elif speed <= 80: data[i] = "small ticket"
    else: data[i] = "big ticket"

for i in range(cases):
    print(data[i])
