primeiro = int(input('Digite primriro número:\n'))
segundo = int(input('Digite o segudo número:\n'))
terceiro =  int(input('Digite o terceiro número:\n'))
#Analisando o menor número
menor = primeiro
if segundo<primeiro and segundo<terceiro:
    menor = segundo
if terceiro<primeiro and terceiro<segundo:
    menor = terceiro
#Analisando o maior número
maior = primeiro
if segundo>primeiro and segundo>terceiro:
    maior = segundo
if terceiro>primeiro and terceiro>segundo:
    maior = terceiro
print('O menor número é {}\nO maior número é {}'.format(menor , maior))
