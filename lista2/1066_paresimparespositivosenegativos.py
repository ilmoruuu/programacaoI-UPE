par = 0
impar = 0
positivo = 0
negativo = 0

for valores in range(5):
    valor = int(input())
    if valor % 2 == 0:
        par = par + 1

    else:
        impar = impar + 1

    if valor > 0:
        positivo = positivo + 1

    elif valor < 0:
        negativo = negativo + 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')