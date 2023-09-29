cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    d = input().rstrip().split(" ")
    formatType = d.pop(0)
    if formatType == "concatenate": data[i] = ','.join(d)
    elif formatType == "formatDate":
        year, month, day = d
        data[i] = year.zfill(4) + month.zfill(2) + day.zfill(2)
    elif formatType == "formatHeight": data[i] = f"{d[0]}'{d[1]}\""

for i in range(cases): print(data[i])
