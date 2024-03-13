hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

hora_total = hora_final - hora_inicial
minuto_total = minuto_final - minuto_inicial

if minuto_total < 0:
    hora_total -= 1
    minuto_total += 60
if hora_total < 0:
    hora_total += 24
if hora_total == 0 and minuto_total == 0:
    hora_total += 24
    
print("O JOGO DUROU", hora_total, "HORA(S) E", minuto_total, 'MINUTO(S)')
