hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

if hora_inicial < hora_final and minuto_inicial < minuto_final:
    duracao = hora_final - hora_inicial
    duracao1 = minuto_final - minuto_inicial
elif hora_inicial > hora_final and minuto_inicial > minuto_final:
    duracao = 24 - hora_inicial + hora_final
    duracao1 = 60 - minuto_inicial +  minuto_final
else:  
    duracao = 24
    duracao1 = 0

print("O JOGO DUROU", duracao, "HORA(S) E", duracao1, 'MINUTO(S)')
