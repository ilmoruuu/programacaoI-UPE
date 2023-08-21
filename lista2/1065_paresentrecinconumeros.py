valorespares = 0

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        valorespares += 1

print(f'{valorespares} valores pares')
