frase = str(input('Olá, seja bem vindo! \n Digite uma frase: \n ')).upper().strip()
print(' A letra A aparece {} vazes na frase. \n ' .format(frase.count('A')))
print(' A primeira letra A apareceu na posição {} \n ' .format(frase.find('A')+1))
print(' A última letra A apareceu na posição {} \n ' .format(frase.rfind('A')+1))