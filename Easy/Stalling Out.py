cases = int(input().rstrip())
data = [""] * cases
for i in range(cases):
    plane, port, star = list(map(float, input().rstrip().split(" ")))
    if abs(port - star) > 5: data[i] = "WARNING"
    elif (port + star) / 2 - plane >= 2: data[i] = "ALARM"
    else: data[i] = "OK"
    
for i in range(cases): print(data[i])