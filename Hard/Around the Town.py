import math

cases = int(input().rstrip())


def dist(p0, p1): 
    return math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)

def mean(arr):
    total = [0] * len(arr)
    count = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            count[i] += 1
            total[i] += arr[i][j]
        total[i] /= count[i]
    return total

def variance(arr):
    total = [0] * len(arr)
    count = [0] * len(arr)
    m = mean(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            total[i] += arr[i][j] - m[i]
            count[i] += 1
        total[i] /= count[i]
    return math.sqrt(total[0]**2 + total[1]**2)

data = [0] * cases
for i in range(cases):
    print(variance([[0, 0], [1, 0]]))
    # L, S = list(map(int, input().rstrip().split(" ")))
    # landmarks = [[]] * 2
    # for j in range(L):
    #     a = list(map(int, input().rstrip().split(" ")))
    #     landmarks[0].append(a[0])
    #     landmarks[1].append(a[1])

    # stops = [[]] * 2
    # for j in range(S):
    #     a = list(map(int, input().rstrip().split(" ")))
    #     stops[0].append(a[0])
    #     stops[1].append(a[1])
    
    # print(variance(landmarks))
    # clusters = [[]] * S
