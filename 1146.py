while True:
    X = int(input())
    if X == 0:
        break
    for c in range(1, X + 1):
        if c < X:
            print(c, end=' ')
        else:
            print(c)

#Para todos os números de 1 a X-1 (i < X), imprime o número seguido de um espaço (end=' ').
#Para o último número X (else), imprime o número sem espaço e termina a linha.