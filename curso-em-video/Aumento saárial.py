salario = float(input('Digite o salário atual R$: '))
if salario <= 1300:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O salário anterior era R${:.2f} com o reajuste passa a ser R${:.2f}'.format(salario, novo))