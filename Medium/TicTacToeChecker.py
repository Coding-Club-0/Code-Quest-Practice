cases = int(input().rstrip())

def check(state):
    # s = [*state]
    b = [0] * 3
    for i in range(3): b[i] = [0] * 3

    for i in range(len(state)): 
        i1 = i // 3   
        j1 = i % 3

        if state[i] == "X": b[i1][j1] = 1
        elif state[i] == "O": b[i1][j1] = -1
        else: b[i1][j1] = 0

    for i in range(3):
        count = 0
        for j in range(3):
            count += b[i][j]
        if count == 3:
            return "X WINS"
        elif count == -3:
            return "O WINS"
    
    for i in range(3):
        count = 0
        for j in range(3):
            count += b[j][i]
        if count == 3:
            return "X WINS"
        elif count == -3:
            return "O WINS"
        
    count1 = 0
    count2 = 0
    for i in range(3):
        count1 += b[i][i]
        count2 += b[3-i-1][i]

    if count1 == 3 or count2 == 3:
        return "X WINS"
    elif count1 == -3 or count2 == -3:
        return "O WINS"

    

    return "TIE"


states = [""] * cases
for i in range(cases):
    states[i] = input().rstrip()

for i in range(cases):
    print(states[i] + " = " + check(states[i]))
