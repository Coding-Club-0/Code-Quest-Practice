cases = int(input().rstrip())
data = [""] * cases

def convertMins(time):
    hour, min = list(map(int, time.split(":")))
    return hour * 60 + min

def convertHours(mins):
    hours = mins // 60
    minutes = mins % 60

    hrString = "hours"
    minString = "minutes"

    if hours == 1: hrString = "hour"
    if minutes == 1: minString = "minute"

    if minutes == 0: return f'{hours} {hrString}'
    if hours == 0: return f'{minutes} {minString}' 
    return f"{hours} {hrString} {minutes} {minString}"


for i in range(cases):
    d = input().rstrip().split(",")
    name = d[0]
    total = 0
    for j in range(1, len(d)): total += convertMins(d[j])
    data[i] = f'{name}={convertHours(total)}'

for i in range(cases): print(data[i])
        
    