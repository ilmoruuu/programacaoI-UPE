seg = int(input())
horas = seg//3600
segundos = seg % 3600
minutos = segundos//60
segundos = segundos % 60

print(f'{horas}:{minutos}:{segundos}')
