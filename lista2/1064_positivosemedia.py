valorespositivos = 0
soma = 0

for i in range(6):
    x = float(input())
    if x >= 0:
        valorespositivos += 1
        soma = soma + x

media = soma/valorespositivos
print(f'''{valorespositivos} valores positivos
{media:.1f}''')
