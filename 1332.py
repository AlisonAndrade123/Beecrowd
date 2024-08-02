casos_testes = int(input())
for testes in range(casos_testes):
    n = str(input())
    cont_one = 0
    cont_two = 0
    
    if len(n) > 3:
        print(3)
    else:
        if n[0] == 'o':
            cont_one += 1
        if n[1] == 'n':
            cont_one += 1
        if n[2] == 'e':
            cont_one += 1

        if n[0] == 't':
            cont_two += 1
        if n[1] == 'w':
            cont_two += 1
        if n[2] == 'o':
            cont_two += 1
        
        if cont_one >= 2:
            print(1)
        elif cont_two >= 2:
            print(2)
