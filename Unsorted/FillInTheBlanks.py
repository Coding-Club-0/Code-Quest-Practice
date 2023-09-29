cases = int(input().rstrip())
for case in range(cases):
    D, T = list(map(int, input().rstrip().split(' ')))

    fields = {}
    for i in range(D):
        field, value = input().rstrip('\n').split(":", 1)
        fields[field] = value[1:]

    # lines = []
    for i in range(T):
        line = input().rstrip()
        for field in fields:
            search = f'[{field}]'
            if search in line:
                first_half = line[:line.index(search)]
                second_half = line[line.index(search)+len(search):]
                line = first_half + fields[field] + second_half
        # lines.append(line)
        print(line)
    
    # print('\n'.join(lines).rstrip())
