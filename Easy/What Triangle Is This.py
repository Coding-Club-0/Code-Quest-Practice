cases = int(input().rstrip())
data = [""] * cases
for i in range(cases):
    side1, side2, side3 = list(map(int, input().rstrip().split(", ")))
    a = side3 >= side1 + side2
    b = side1 >= side2 + side3
    c = side2 >= side1 + side3

    if a or b or c: 
        data[i] = "Not a Triangle"
        continue
    
    if side1 == side2 and side2 == side3: data[i] = "Equilateral"
    elif side1 != side2 and side2 != side3 and side1 != side3: data[i] = "Scalene"
    else: data[i] = "Isosceles"

for i in range(cases): print(data[i])