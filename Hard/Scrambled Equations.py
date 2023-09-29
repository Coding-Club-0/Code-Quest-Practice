from itertools import *
# from decimal import * 

cases = int(input().rstrip())
data = [""] * cases


def calculate_expression(numbers, operations):
    result = numbers[0]
    for i in range(len(operations)):
        if operations[i] == '+':
            result += numbers[i + 1]
        elif operations[i] == '-':
            result -= numbers[i + 1]
        elif operations[i] == '*':
            result *= numbers[i + 1]
        elif operations[i] == '/':
            result /= numbers[i + 1]
    return result

def can_combine_to_target(M, numbers, operations):
    for num_permutation in permutations(numbers):
        for ops_permutation in permutations(operations):
            if calculate_expression(num_permutation, ops_permutation) == M:
                return True
    return False

for i in range(cases):
    d = input().rstrip().split(":")
    result = int(d[0])
    d[1] = d[1].split(" ")

    nums = []
    operations = []
    for j in range(len(d[1])):
        try: nums.append(int(d[1][j]))
        except: operations.append(d[1][j])
    print(nums)
    print(operations)
    data[i] = str(can_combine_to_target(result, nums, operations)).upper()
for i in range(cases): print(data[i])