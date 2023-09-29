cases = int(input().rstrip())
for i in range(cases):
    C, T = list(map(int, input().rstrip().split(" ")))
    budgetItems = []
    budgetPrices = []
    for j in range(C):
        data = input().rstrip().split(" ")
        budgetItems.append(data[0])
        budgetPrices.append(int(data[1]))

    for j in range(T):
        data = input().rstrip().split(" ")
        index = budgetItems.index(data[0])
        add = data[1] == "+"
        price = int(data[2])
        if add: budgetPrices[index] += price
        else: budgetPrices[index] -= price

        if budgetPrices[index] < 0:
            print("NO")
            budgetPrices[index] += price
        else: print("YES") 