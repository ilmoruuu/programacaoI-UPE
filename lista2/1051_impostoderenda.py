renda = float(input())

if renda > 0 and renda <= 2000:
    print('Isento')

elif renda > 2000 and renda <= 3000:
    resto = renda - 2000
    resultado = resto * 0.08
    print(f'R$ {resultado:.2f}')

elif renda > 3000 and renda < 4500:
    resto = renda - 3000
    resultado = (resto * 0.18) + (1000 * 0.08)
    print(f'R$ {resultado:.2f}')

else:
    resto = renda - 4500
    resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print(f'R$ {resultado:.2f}')
