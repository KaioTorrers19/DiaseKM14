dias = int(input('quantos dias alugados?'))
km = float(input('quantos KM rodados? '))
pago = (dias*60) + (km* 0.15)
print('o valor total será R${}!'.format(pago))