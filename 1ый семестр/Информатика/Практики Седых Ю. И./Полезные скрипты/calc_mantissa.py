from decimal import Decimal

a = Decimal('0.625')
o = []
for _ in range(30):
    new = a * 2
    if new >= 1: 
        print(new)
        o.append('1')
    else: 
        print(new)
        o.append('0')
    a = new % 1
    if a == 0:
        break
print(''.join(o))