data1, dia1 = input().split()
dia1 = int(dia1)
hr1, m1, s1 = list(map(int, input().split()))

data2, dia2 = input().split()
dia2 = int(dia2)
hr2, m2, s2 = list(map(int, input().split()))

segundos = s2-s1
minutos = m2 - m1
horas = hr2-hr1
dias = dia2 - dia1

if segundos <0:
    segundos += 60
    minutos -= 1

if minutos <0:
    minutos += 60
    horas -= 1

if horas <0:
    horas += 24
    dias -= 1

print(f'''{dias} dia(s)
{horas} hora(s)
{minutos} minuto(s)
{segundos} segundo(s)''')