from datetime import date
print('\33[30mO alistamento militar para o jovem do sexo masculino é obrigatório, a partir dos 18 anos.\nDeve se alistar nos seis primeiros meses (janeiro a junho) do ano em que completar dezoito anos.')
ano = date.today().year
data = int(input('\33[37mDigite Ano de nascimento: '))
idade = ano - data
print(f'Quem nasceu em \33[30m{data} \33[37mtem \33[30m{idade} anos \33[37mem \33[3m{ano}')
if idade == 18:
    print('\33[30mVocê deve fazer o alistamento esse ano.')
elif idade < 18:
    analise = 18 - idade
    print(f'\33[37mVocê deve se alista em \33[30m{analise} ano(s)')
    atual = ano + analise
    print(f'Você tem que se alistar em \33[37m{atual}')
elif idade > 18:
    analise = idade - 18
    print(f'\33[37mVocê deveria ter se alistado há \33[37m{analise} anos')
    atual = ano - analise
    print(f'Você deveria ter se alistado em {atual}')
