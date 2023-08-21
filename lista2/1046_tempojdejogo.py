a, b = list(map(int, input().split()))

if a < b:
    print(f'O JOGO DUROU {b-a} HORA(S)')

elif a > b:
    print(f'O JOGO DUROU {(24-a)+b} HORA(S)')

if a == b:
    print(f'O JOGO DUROU {24} HORA(S)')
