"""
Faça um programa que leia o horario em (hora, minuto e segundo( de inicio e a duração em segundos de uma experiencia
quimica. O programa deve resultar em com novo horario em (hora, minuto e segundo( com o termino da mesma
"""
# marcar o inicio da experiencia, e depois ir calculando até o final da experiencia

print("Digite o horario inicial da experiencia quimica: ")
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

d = int(input("Duração da experiencia em (segundos): "))  # pensei usar \n pra fazer uma quebra de linha
# em cima não sabia se botava um calculo pra somar as horas, minutos e segundos e aparecer o total em segundos

hora_final = h_final = (horas + (minutos + (segundos+d)//60)//60) % 24
minuto_final = (minutos + (segundos+d)//60) % 60
segundo_final = (segundos + d) % 60

print(f"A experiencia acabará as {hora_final} horas, {minuto_final} minutos e {segundo_final} segundos")
