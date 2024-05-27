notas_validas = soma_notas = 0

while True:
    nota = float(input())
    if nota < 0 or nota > 10 :
        print('nota invalida')
    else:
        soma_notas += nota
        notas_validas += 1
        if notas_validas == 2:
            media = soma_notas / 2
            print(f'media = {media:.2f}')
            break