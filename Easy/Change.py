cases= int(input().rstrip())

data = [""] * cases
for i in range(cases):
    data[i] = input().rstrip()

for i in range(cases):
    value = float(data[i][1:])
    values = [0.25, 0.1, 0.05, 0.01]
    counts = [0, 0, 0, 0]
    names = ["Quarters", "Dimes", "Nickels", "Pennies"]

    current = 0
    while True:
        if round(value, 3) >= values[current]:
            value -= values[current]
            counts[current] += 1
        else:
            current += 1
        if current >= len(values): 
            break
    print(data[i])
    for j in range(len(counts)):
        print(names[j] + "=" + str(counts[j]))
