entrada = 1
while entrada > 0:
    entrada: int(input())
    pacotes = list(map(int, input().split()))
    tempo = list(map(int, input().split()))

    tempototal = 0
    for i in range(entrada -1, 0, -1):
        for j in range(i):
            pacoteatual = pacotes[j]
            tempoatual = tempo[j]
            if pacotes[j] > pacotes[j+1]:
                pacotes[j] = pacotes[j+i]
                pacotes[j+1] = pacoteatual
                tempo[j] = tempo[j+i]
                tempo[j+i] = tempoatual
                tempototal += (tempo[j]+tempo[j+1])

print(tempototal)
