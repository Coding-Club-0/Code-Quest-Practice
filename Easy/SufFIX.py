cases = int(input().rstrip())
data = [""] * cases

for i in range(cases): 
    d = input().rstrip()[:-2]
    n = int(d)
    last = n % 10
    last2 = n % 100

    if last == 1: data[i] = f"{d}st"
    elif last == 2: data[i] = f"{d}nd"
    elif last == 3: data[i] = f"{d}rd"
    else: data[i] = f"{d}th"
    
    if last2 >= 11 and last2 <= 13: data[i] = f"{d}th"
for i in range(cases): print(data[i].strip())