cod, quant = map(float, input().split())

valor = 0
if cod == 1:
    valor = 4.00

elif cod == 2:
    valor = 4.50

elif cod == 3:
    valor = 5.00

elif cod == 4:
    valor = 2.00

elif cod == 5:
    valor = 1.50

print(f'Total: R$ {valor*quant:.2f}')