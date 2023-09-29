cases = int(input().rstrip())

# def drawLine(x1, y1, x2, y2, grid):
#     dir = [x2-x1, y2-y1]
#     reachedEnd = True
#     for i in range(0, 100):
#         t = i/100
#         x = round(x1 + dir[0] * t)
#         y = round(y1 + dir[1] * t)
        
#         if grid[x][y] == "#":
#             reachedEnd = False
#             break
#     return reachedEnd

def drawLine(x1, y1, x2, y2, grid):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    while x1 != x2 or y1 != y2:
        if grid[x1][y1] == "#":
            return False
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    
    return True



data = [''] * cases
for i in range(cases):
    d = list(map(int, input().rstrip().split(" ")))
    h, w, num = d
    grid = [''] * h

    for j in range(h):
        grid[j] = [*input().rstrip().ljust(w, ' ')]
    
    locations = [''] * (num + 1)
    for j in range(h):
        for k in range(w):
            try: locations[int(grid[j][k])] = [j, k]
            except: continue
    valid = []
    for j in range(1, num+1):
        if drawLine(locations[0][0], locations[0][1], locations[j][0], locations[j][1], grid): valid.append(str(j))

    data[i] = ' '.join(valid)

for i in range(cases):   
    if len(data[i]) == 0: print("No viable locations")
    else: print(data[i])