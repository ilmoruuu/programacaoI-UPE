salario = float(input())
au15 = (15/100)
au12 = (12/100)
au10 = (10/100)
au7 = (7/100)
au4 = (4/100)


if 0 <= salario <= 400:
 print(f'Novo salario: {salario+(salario*au15):.2f}')
 print(f'Reajuste ganho: {salario*au15:.2f}')
 print(f'Em percentual: {au15*100:.0f} %')

elif 400.01 <= salario <= 800:
 print(f'Novo salario: {salario+(salario*au12)}:.2f')
 print(f'Reajuste ganho: {salario*au12:.2f}')
 print(f'Em percentual: {au12*100:.0f}')

if 800.01 <= salario <= 1200.00:
 print(f'Novo salario: {salario+(salario*au10):.2f}')
 print(f'Reajuste ganho: {salario*au10:.2f}')
 print(f'Em percentual: {au10*100:.0f} %')

elif 1200.01 <= salario <= 2000:
 print(f'Novo salario: {salario+(salario*au7):.2f}')
 print(f'Reajuste ganho: {salario*au7:.2f}')
 print(f'Em percentual: {au7*100:.0f} %')

if salario > 2000:
 print(f'Novo salario: {salario+(salario*au4):.2f}')
 print(f'Reajuste ganho: {salario*au4:.2f}')
 print(f'Em percentual: {au4*100:.0f} %')



