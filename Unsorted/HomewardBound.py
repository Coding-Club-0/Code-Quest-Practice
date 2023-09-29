cases = int(input().rstrip())

# Orlando    -> Fort Worth
# Fort Worth -> Denver
# Denver     -> Washington
# Washington -> Toronto


for case in range(cases):
    num = int(input().rstrip())

    locations = []
    stashed = []

    for i in range(num):
        loc1, loc2 = input().rstrip().split(" ")
        added = False
        for j in range(len(locations)):
            if loc1 == locations[j][1]:
                locations.insert(j+1, [loc1, loc2])
                added = True
                break
            elif loc2 == locations[j][0]:
                locations.insert(j, [loc1, loc2])
                added = True
                break

        if len(locations) == 0: 
            locations.append([loc1, loc2])
        elif not added:
            stashed.append([loc1, loc2])


    for i in range(len(stashed)):
        loc1, loc2 = stashed[i]
        for j in range(len(locations)):
            if loc1 == locations[j][1]:
                locations.insert(j+1, [loc1, loc2])
                break
            elif loc2 == locations[j][0]:
                locations.insert(j, [loc1, loc2])
                break

    print(locations[-1][1])
    for i in range(len(locations)-1, -1, -1):
        print(locations[i][0])
