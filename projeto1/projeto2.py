segundos = int(input('Numero em segundos que deseja converter:'))

dias, segundos = divmod(segundos, 86400)
horas, segundos = divmod(segundos, 3600)
minutos, segundos = divmod(segundos, 60)

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos')
#  1minuto tem 60s,1hr tem 3600 segundos e 1 dia tem 86400
#  multiplquei o a quantidade de segundos pela quantidade de minutos, hrs e dia
