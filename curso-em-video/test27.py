import time
velocidade = float(input('   Velocidade atual do carro?\n'))
if velocidade > 60:
    print('           ...ALERTA...')
    time.sleep(5.0)
    print('\n           !!!CUIDADO!!! \n\n           ...DIMINUA... \n\n')
    time.sleep(6.0)
    multa = (velocidade-60) * 10
    print('\n  EEEI VOCÊ ACABA DE SER MULTADO!\n\n      EXCEDEU O LIMETE DA BR\n\n        MULTA DE {:.2f}'.format(multa))




