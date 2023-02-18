nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
print('A soma das notas {:.1f}, {:.1f}, {:.1f} e {:.1f} a média do aluno é {:.1f}' .format( nota1, nota2, nota3, nota4, media))
if 7 > media >= 5:
    print('RECUPERAÇÃO!!!')
elif media < 5:
    print('REPROVADO!!!')
elif media >= 7:
    print('APROVADO!!!')