casos_testes = int(input())
for testes in range(casos_testes):
    n = str(input())

    contador = 0

    for i in range(0, len(n)):
        if n[i] == '1':
            contador += 2
        elif n[i] == '2':
            contador += 5
        elif n[i] == '3':
            contador += 5
        elif n[i] == '4':
            contador += 4
        elif n[i] == '5':
            contador += 5
        elif n[i] == '6':
            contador += 6
        elif n[i] == '7':
            contador += 3
        elif n[i] == '8':
            contador += 7
        elif n[i] == '9':
            contador += 6
        elif n[i] == '0':
            contador += 6

    print(f'{contador} leds')