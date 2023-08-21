name = str(input())
safix = float(input())
vendas = float(input())
comiss = (15/100)*(vendas)
total = (comiss+safix)

print(f'TOTAL = R$ {total:.2f}')