from math import sqrt
x1, y1 = (float(valor) for valor in input().split())
x2, y2 = (float(valor) for valor in input().split())
dif = sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(f'{dif:.4f}')
