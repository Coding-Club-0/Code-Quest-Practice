cases = int(input().rstrip())
data = [""] * cases

letters = "DCBA"
for i in range(cases):
    school = input().rstrip()
    people = int(input().rstrip())
    
    names = [""] * people
    totals = [""] * people
    counts = [""] * people
    for j in range(people):
        name, grades = input().rstrip().split(":")
        names[j] = name
        grades = grades.split(",")
        total = 0
        count = 0
        for grade in grades:
            letter = grade[0]
            total += ((letters.index(letter) + 1) * int(grade[1]))
            count += int(grade[1])
        totals[j] = total / count
        counts[j] = count
    
    maxValue = totals[0]
    maxIndex = 0

    for j in range(1, people):
        if totals[j] > maxValue: 
            maxIndex = j
            maxValue = totals[j]
    
    ties = []
    for j in range(0, people):
        if totals[j] == maxValue: ties.append(j)
    
    if len(ties) > 1:
        maxCount = counts[0]
        maxCIndex = 0
        for j in range(len(ties)):
            if counts[j] > maxCount:
                maxCount = counts[j]
                maxCIndex = j
        maxIndex = maxCIndex
    
    data[i] = f'{school} = {names[maxIndex]}'

for i in range(cases): print(data[i])