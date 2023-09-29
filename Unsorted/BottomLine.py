companies = ["Cassowary Craft", "Lead Balloons Ltd"]
cases = int(input().rstrip())

for case in range(cases):
    a, b = list(map(int, input().rstrip().split(" ")))

    if a == b:
        print("Cassowary Craft and Lead Balloons Ltd sold the same number of aircraft")
        continue

    print(f"{companies[a < b]} sold {abs(a-b)} more aircraft")

    