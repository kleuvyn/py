import time
numero=int(input('Digite um número com unidade de milhar! \n '))
numero1 = str(numero)
print('\n Analisando o número {} ... \n' .format(numero))
time.sleep(2.0)
print('  ...CAREGANDO...\n')
time.sleep(2.0)
print('Unidade: {}' .format(numero1[3]))
time.sleep(1.0)
print('Dezena: {}' .format(numero1[2]))
time.sleep(1.0)
print('Centena: {}' .format(numero1[1]))
time.sleep(1.0)
print('Unidade de Milhar: {}\n' .format(numero1[0]))
time.sleep(2.0)
print('OBRIGADA!')