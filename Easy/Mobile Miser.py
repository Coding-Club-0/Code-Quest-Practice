from decimal import *
cases = int(input().rstrip())
data = [''] * cases


def roundTo(num, places): return f'%.{places}f' % num.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

for i in range(cases): data[i] = Decimal(input().rstrip()[1:])
for i in range(cases):
    print(f'Total of the bill: ${roundTo(data[i], 2)}'.strip())
    print(f'15% = ${roundTo(Decimal("0.15") * data[i], 2)}'.strip())
    print(f'18% = ${roundTo(Decimal("0.18") * data[i], 2)}'.strip())
    print(f'20% = ${roundTo(Decimal("0.20") * data[i], 2)}'.strip())