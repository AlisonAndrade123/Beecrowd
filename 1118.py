while True:
    notas_validas = 0
    soma_notas = 0

    while notas_validas < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            soma_notas += nota
            notas_validas += 1
        else:
            print('nota invalida')

    media = soma_notas / 2
    print(f'media = {media:.2f}')

    while True:
        print('novo calculo (1-sim 2-nao)')
        opcao = int(input())
        if opcao == 1 or opcao == 2:
            break

    if opcao == 2:
        break
