número1 = int(input('Digite op primeiro número: '))
número2 = int(input('Digite o segundo número: '))
if número1 > número2:
    print('O Primeiro é o maior número {} '.format(número1))
elif número2 > número1:
    print('O segundo é o maior nuḿero {}'.format(número2))
else:
    print('Ambos números são iguai {} = {}'.format(número1, número2))