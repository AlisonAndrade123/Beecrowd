hora_inicial, hora_final = map(int, input().split())

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
elif hora_inicial > hora_final:
    duracao = 24 - hora_inicial + hora_final
else:  
    duracao = 24

print("O JOGO DUROU", duracao, "HORA(S)")
