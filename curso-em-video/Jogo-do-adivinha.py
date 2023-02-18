import time
from random import randint
computador = randint(0, 100)
print('____.__' * 5)
print('Vou pensar em um número de 0 a 100.\n Tente divinhar...')
print('____.__ ' * 5 )
print('\n....PENSANDO.... =^_^=\n')
time.sleep(2.5)
jogador = int(input('Eii qual número eu pensei?\n'))
time.sleep(3.0)
if jogador == computador:
    print('Parabéns!!!\n \nVocê acertou!')
else:
    print('Ganhei!!!\n \nEu pensei no Número {} e não no {} !' . format(computador, jogador))

