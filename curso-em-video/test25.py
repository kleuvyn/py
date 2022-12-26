#PARTE1
idade = int(input('Digite a sua idade:\n '))
if idade<=18:
    print('MENOR DE 18 ANOS')
else:
    print('MAIOR DE 18 ANOS')
print("...FIM...")

#PARTE2
tempo = int(input('Digite quantos anos tem o seu carro:\n '))
print('carro novo' if tempo<=5 else'carro velho')

#PARTE3
n = str(input('Olá, \nSeja bem vindo!\nInforme o seu nome completo?\n ')).strip().upper()
nome = n.split()
print('Oi {} {}, agora vamos analisar o seu nome.\n' .format(nome[0], (nome[len(nome)-1])))
bimestre1 = float(input('Digite a sua nota do 1ª Bimestre:'))
bimestre2 = float(input('Digite a sua nota do 2ª Bimestre:'))
bimestre3 = float(input('Digite a sua nota do 3ª Bimestre:'))
bimestre4 = float(input('Digite a sua nota do 4ª Bimestre:'))
nota = ( bimestre1 + bimestre2 + bimestre3 + bimestre4)/4
print('Sua media foi {:.2f}'  .format(nota))
print('Parabéns sua nota está acima da média' if nota>=7  else 'Infelizmente sua nota está abaixo da média')

#Parte4