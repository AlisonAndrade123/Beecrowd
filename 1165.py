casos_de_teste = int(input())  
for t in range(casos_de_teste):
    n = int(input())
    
    eh_primo = True
    for i in range(2, n):
        if n % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(f'{n} eh primo')
    else:
        print('')