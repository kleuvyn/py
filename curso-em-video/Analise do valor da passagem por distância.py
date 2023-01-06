distancia = float(input('Qual é a distÂncia da sua viagem?'))
print('A sua viagem de {}Km'.format(distancia))
if distancia <=200:
    valor = distancia * 0.98
else:
    valor = distancia * 0.48
print('A sua sua passagem será de R${:.2F}'.format(valor))