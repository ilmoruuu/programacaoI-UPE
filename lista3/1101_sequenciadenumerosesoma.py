while True:
    m, n = list(map(int, input().split()))

    soma = 0
    lista = []
    menor = min(m, n)
    maior = max(m, n)

    if m <= 0 or n <= 0:
        break

    for i in range(menor, maior+1):
        soma += 1
        lista.append(i)

    for x in lista:
        print(x, end=' ')

    print(f'Sum= {soma}')