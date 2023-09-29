cases = int(input().rstrip())
data = [''] * cases
from fractions import Fraction

def continued_fraction(decimal):
    a = int(decimal)
    b = Fraction(decimal - a)
    fractions = [str(a)]
    for i in range(9):
        reciprocal = Fraction(b.denominator, b.numerator)
        a = int(reciprocal)
        b = reciprocal - a
        fractions.append(str(a))
        if float(b) < 10e-4:
            break
    return ' '.join(fractions)

for i in range(cases):
    value = float(input().rstrip())
    # nums = [str(int(value))]

    # nextValue = value
    # count = 0
    # while count < 10:
    #     if nextValue % 1 < 10e-4: 
    #         break
    #     nextValue = 1 / (nextValue % 1)
    #     nums.append(str(int(nextValue)))
    #     count += 1
    
    # data[i] = ' '.join(nums)
    data[i] = continued_fraction(value)

for i in range(cases): print(data[i])

