cases = int(input().rstrip())

for case in range(cases):
    W, L, S = map(int, input().rstrip().split(" "))
    R = int(input().rstrip())
    rules = []
    for i in range(R):
        rowStart, col = map(int, input().rstrip().split(" "))
        rules.append([rowStart, col])

    moves = input().rstrip('\n')

    print("="*(W+2))

    rows = [0] * (L)
    currentPos = S-1

    print('|' + ' '*currentPos + 'v' + ' '*(W-currentPos-1) + '|')
    print('-'*(W+2))

    crashed = False
    for i in range(L):
        if moves[i] == "L":
            currentPos -= 1
        elif moves[i] == "R":
            currentPos += 1

        currentPos = max(0, currentPos)
        currentPos = min(W, currentPos)

        rows[i] = currentPos
        string = '|' + ' '*currentPos + 'v' + ' '*(W-currentPos-1) + '|'

        for j in range(len(rules)):
            start, col = rules[j]

            if (i+1) % (start) == 0 and i > 0:
                string = [*string]
                if string[col] == 'v':
                    string[col] = "X"
                    crashed = True
                else:
                    string[col] = "o"
                string = ''.join(string)
            if crashed: break
        
        print(string)
        if crashed: break

    if crashed:
        print("You Crashed - GAME OVER")
        continue

    print("="*(W+2))
    print("Course Complete!")

