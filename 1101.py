while True:
    m, n = map(int, input().split())
    
    if m <= 0 or n <= 0:
        break
    cont = 0
    if m > n:
        for c in range(n, m+1):
            cont += c
            print(f'{c}', end = ' ')
        print(f'Sum={cont}')
    elif n > m:
        for c in range(m, n+1):
            cont += c
            print(f'{c}', end = ' ')
        print(f'Sum={cont}')