a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    a, b = b, a

if (b%a) == 0:
    print('Sao Multiplos')

else:
    print('Nao sao Multiplos')