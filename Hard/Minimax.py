import math

def score(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "*":
            return 1 if board[i] == "X" else -1
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "*":
            return 1 if board[i] == "X" else -1
    if board[0] == board[4] == board[8] and board[0] != "*":
        return 1 if board[0] == "X" else -1
    if board[2] == board[4] == board[6] and board[2] != "*":
        return 1 if board[2] == "X" else -1
    if "*" not in board:
        return 0
    return None

def player(state):
    xs = state.count("X")
    os = state.count("O")
    if os > xs:
        return "O"
    
    return "X"

def actions(state):
    a = []
    for i in range(len(state)):
        if state[i] == "*":
            a.append(i)
    return a

def result(state, action):
    a = list(state)
    a[action] = player(state)
    return ''.join(a)

def minimax(state):
    v = score(state)
    if v is not None:
        return v

    if player(state) == "X":
        value = -math.inf
        for a in actions(state):
            value = max(value, minimax(result(state, a)))
        return value
    else:
        value = math.inf
        for a in actions(state):
            value = min(value, minimax(result(state, a)))
        return value

def next_move(state):
    best_value = None
    best_action = None
    current_player = player(state)
    act = actions(state)
    act.sort()
    for action in act:
        new_state = result(state, action)
        new_value = minimax(new_state)
        
        if score(new_state) == (1 if current_player == "X" else -1):
            return action

        if best_value is None or (current_player == "X" and new_value > best_value) or (current_player == "O" and new_value < best_value):
            best_value = new_value
            best_action = action
            
    return result(state, best_action)

cases = int(input().rstrip())
data = [""] * cases
for i in range(cases):
    string = ""
    for j in range(3):
        string += input().rstrip()
    optimal_move = next_move(string)
    
    for j in range(0, 9, 3):
        data[i] += optimal_move[j:j+3] + "\n"
    
for i in range(cases): print(data[i].rstrip())