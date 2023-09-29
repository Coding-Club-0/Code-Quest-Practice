cases = int(input().rstrip())

donorValues = [""] * cases

def inArray(name, arr):
    for n in arr:
        if n == name:
            return True
    return False

for i in range(cases):
    list1 = input().rstrip().split(",")
    list2 = input().rstrip().split(",")

    donorValues[i] = [""] * 3
    for j in range(3): donorValues[i][j] = []

    
    for j in range(len(list1)):
        inBoth = True
        for k in range(len(list2)):
            if list1[j] == list2[k]:
                donorValues[i][1].append(list1[j])
                inBoth = False
                break
        if inBoth: donorValues[i][0].append(list1[j])

    for j in range(len(list2)):
        inBoth = True
        for k in range(len(list1)):
            if list1[k] == list2[j]:
                inBoth = False
                break
        if inBoth: donorValues[i][2].append(list2[j])


for i in range(cases):
    for j in range(len(donorValues[i])):
        donorValues[i][j].sort()
        print(str(donorValues[i][j]).replace("[", "").replace("]", "").replace(", ", ",").replace("'", ""))
            



