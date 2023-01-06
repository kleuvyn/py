valor = float(input('Valor no imovel:'))
salário = float(input('Valor do salário:'))
tempo = int(input('Quanto tempo de financiamento:'))
ideal = salário * 35 / 100
prestação = valor / (tempo * 12)
salário35 = salário * 35 / 100
juros = prestação * 75 / 100 + prestação
print('Para uma casa de {:.2f} para o financiamento de {:.2f}anos com prestações de {:.2f}' .format(valor, tempo , juros))
if prestação <= ideal:
    print('Concedido')
else:
    print('Negado')
