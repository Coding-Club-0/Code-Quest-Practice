import copy

cases = int(input().rstrip())

generations = [0] * cases
boards = [""] * cases

for i in range(cases):
    generations[i] = int(input().rstrip())
    board = [""]
    count = 0
    while count < len(board):
        arr = [*input().rstrip()]
        if count == 0: board = [""] * len(arr)
        board[count] = arr
        count += 1
    boards[i] = board

def insideRect(x1, y1, x, y, w, h):
    return x1 >= x and x1 <= x + w and y1 >= y and y1 <= y + h

def checkAdj(arr, i, j):
    count = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if not (k == 0 and l == 0) and insideRect(i+k, j+l, 0, 0, len(arr)-1, len(arr[0])-1) and arr[i+k][j+l] == "1": count += 1
    return count

def nextState(arr):
    new = copy.deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            count = checkAdj(arr, i, j)
            if arr[i][j] == "1":
                if not (count == 2 or count == 3): new[i][j] = "0"
            elif arr[i][j] == "0" and count == 3: new[i][j] = "1"
    
    return new

for i in range(cases):
    board = boards[i]
    for j in range(generations[i]):
        nextBoard = nextState(board)
        board = nextBoard
    for j in range(len(board)):
        print(''.join(board[j]).strip())
