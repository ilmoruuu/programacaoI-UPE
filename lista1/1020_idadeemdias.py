dias = int(input())
anos = dias//365
dias = dias % 365
mes = dias//30
dias = dias % 30

print(f'{anos} ano(s)\n'
      f'{mes} mes(es)\n'
      f'{dias} dia(s)')
