cases = int(input().rstrip())
data = []
for i in range(cases):
    data.append(input().rstrip())

names = [0] * cases
results = [0] * cases
for i in range(cases):
    d = data[i].split(":")
    names[i] = d[0]
    results[i] = d[1]

checks = ["1B", "2B", "3B", "HR"]
def occurences(arr, string):
    count = 0
    for i in range(len(arr)):
        if arr[i] == string: count += 1
    return count

for i in range(cases):
    d = results[i].split(",")
    total = 0
    for j in range(len(checks)):
        total += occurences(d, checks[j]) * (j + 1)
    divisor = (len(d)-occurences(d, "BB"))
    if divisor == 0: result = 0
    else: result = round(total/divisor, 3)
    print(names[i] + "=" + '%.3f' % (result))
    
    

    


