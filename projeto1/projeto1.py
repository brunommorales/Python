"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um
 deu para a realização da aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio e imprima quanto cada um ganharia do prêmio
 com base no valor investido.
"""

premio = float(input('Quanto foi o prêmio da loteria?\n'))

Bruno = float(input('Quanto investiu o apostador Bruno (valor maior)? '))
Erick = float(input('Quanto investiu o apostador Erick (valor médio)? '))
Cassiano = float(input('Quanto investiu o apostador Cassiano (valor menor)? '))

total = Bruno + Erick + Cassiano

print('Bruno tem {} % do total'.format((Bruno / total) * 100))
print('Erick tem {} % do total'.format((Erick / total) * 100))
print('Cassiano tem {} % do total'.format((Cassiano / total) * 100))

resultado_Bruno = Bruno / total * premio
resultado_Erick = Erick / total * premio
resultado_Cassiano = Cassiano / total * premio

print('Resultado Bruno {}'.format(resultado_Bruno))
print('Resultado Erick {}'.format(resultado_Erick))
print('Resultado Cassiano {}'.format(resultado_Cassiano))
