valores = list(map(float, input().split()))
a, b, c = valores

perimetro = (a + b + c)
area_trap = ((a + b) * c) / 2

if (a < (b + c)) and (b < (c + a)) and (c < (b + a)):
    print(f'Perimetro = {perimetro:.1f}')

else:
    print(f'Area = {area_trap:.1f}')
