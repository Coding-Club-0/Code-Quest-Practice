cases = int(input().rstrip())
for case in range(cases):
    values0 = list(map(float, input().rstrip().split(" ")))
    values1 = list(map(float, input().rstrip().split(" ")))

    events = []
    for i in range(len(values0)):
        if values0[i] >= 0.6 and values1[i] >= 0.6 and values0[i] <= 0.85 and values1[i] <= 0.85:
            events.append(str(i))
    
    if len(events) == 0:
        print("No multipaction events detected.")
    elif len(events) == 1:
        print(f'A multipaction event was detected at time index {events[0]}.')
    else:
        print(f'{len(events)} multipaction events were detected at time indices: {" ".join(events)}.')
