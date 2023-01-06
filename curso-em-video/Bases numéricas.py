número = int(input('Digite um número: '))
print('''Escolha para qual base deseja converter
[1] Binário
[2] Octal
[3] Hexadecimal''')
alternativa =  int(input('Alternativa: '))
if alternativa == 1:
    print('{} para Binário é {}'.format(número, bin(número)[2:]))
elif alternativa == 2:
    print('{} para Octalé {}'.format(número, oct(número)[2:]))
elif alternativa == 3:
    print('{} para Hexadeciamal é {}'.format(número, hex(número)[2:]))
else:
    print('OPÇÃO INAVALIDA \nTENTE NOVAMENTE' )
