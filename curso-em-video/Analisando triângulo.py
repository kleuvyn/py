reta1 = float(input('Primero segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta1 and reta3 < reta1 + reta2:
    print('Os segmentos acima Podem Formar um Triângulo')
else:
    print('Os segmentos acima Não Podem Formar um Triãngulo')