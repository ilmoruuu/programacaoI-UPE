cedulas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())

print(valor)
for cedula in cedulas:
    qntd_cedulas = int(valor/cedula)
    valor -= qntd_cedulas * cedula
    print(f'{qntd_cedulas} nota(s) de R$ {cedula},00')
