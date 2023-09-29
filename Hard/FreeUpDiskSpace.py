from datetime import datetime
cases = int(input().rstrip())

sizes = [0] * cases
totalSizes = [0] * cases
scores = [0] * cases

currentTime = datetime(2019, 4, 27, 0, 0)
for i in range(cases):
    d = input().strip().split(" ")
    files = int(d[0])
    size = float(d[1])
    totalSizes[i] = size
    sizes[i] = [""] * files
    scores[i] = [""] * files
    for j in range(files):
        data = input().rstrip().split(" ")
        date = data[0].split("/")
        hour = 0
        isAfternoon = int(data[2] == "PM")
        time = datetime(int(date[2]), int(date[1]), int(date[0]), hour, 0, 0)
        sizes[i][j] = int(data[3])
        scores[i][j] = [((currentTime - time).days - 0.5*isAfternoon) * sizes[i][j] / 1000, data[4]]

def key(input):
    return input[0] 

for i in range(cases):
    scores[i].sort(reverse=True, key=key)

for i in range(cases):
    size = 0
    index = 0
    while size <= totalSizes[i]/4:
        try:
            value = scores[i][index]
            print((value[1] + " " + ('%.3f' % round(value[0], 3))).strip())
            index += 1
            size += sizes[i][index] / (10**6)
        except: break