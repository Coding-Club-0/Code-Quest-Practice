cases = int(input().rstrip())
data = ["No"] * cases

def inRect(x1, y1, x, y, w, h): return x1 >= x and x1 <= x + w and y1 >= y and y1 <= y + h

for i in range(cases):
    R, C = list(map(int, input().rstrip().split(",")))
    r1, c1 = list(map(int, input().rstrip().split(",")))
    r2, c2 = list(map(int, input().rstrip().split(",")))

    if inRect(r1, c1, 1, 1, R-1, C-1) and inRect(r2, c2, 1, 1, R-1, C-1): 
        dx = r2 - r1
        dy = c2 - c1
        if abs(dx) == abs(dy): data[i] = "Yes"
        else: data[i] = "No"
    else: data[i] = "No"

for i in range(cases): print(data[i])
    