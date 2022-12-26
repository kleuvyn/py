nome = str(input('Digite o seu nome completo?\n ')).strip()
print('O seu nome tem Silva? {} \n' .format('SILVA' in nome.upper()))
pais = str(input('Em que país você nasceu?\n ')).strip()
print(pais[:7].upper() == 'BRASIL')
regiao = str(input('Digite o sua região: \n')).strip()
print('Sua região é a {} ?' .format('MATO GROSSO', 'MATO GROSSO DO SUL, GOIS', 'BRASILIA' in regiao.upper()))
#organizar ideias arrumar codigo

