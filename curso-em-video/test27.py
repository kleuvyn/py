velocidade = float(input('Velocidade atual do carro?\n'))
if velocidade > 55:
    print('...DIMINUA A VELOCIDADE...')
if velocidade > 60:
    multa = (velocidade-60) * 10
    print('\nEEEI VOCÊ ACABA DE SER MULTADO!\nEXCEDEU O LIMETE DA BR\nMULTA DE {:.2f}'.format(multa))




