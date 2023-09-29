cases = int(input().rstrip())

def calculateSunday(y):
    a = y % 19
    b = y % 4
    c = y % 7
    k = int(y / 100)
    p = int((13 + 8*k) / 25)
    q = int(k / 4)
    m = (15 - p + k - q) % 30
    n = (4 + k - q) % 7
    d = (19 * a + m) % 30
    e= (2*b + 4*c + 6*d + n) % 7
    f = (11 * m + 11) % 30
    date = 22 + d + e
    if date <= 31: return f"{y}/03/" + str(date).zfill(2)
    else:
        if d == 28 and e == 6 and f < 19: return f"{y}/04/18"
        elif d == 29 and e == 6: return f'{y}/04/19'
        return  f'{y}/04/' + str(date-31).zfill(2)

results = [''] * cases
for i in range(cases):
    results[i] = calculateSunday(int(input().rstrip()))

# use this code to find when the next easter will be on a certain day
# year = 2023
# while True:
#     year += 1
#     result = calculateSunday(year)
#     if result == f'{year}/04/15': 
#         print(result)
#         break

for i in range(cases):
    print(results[i])
        



