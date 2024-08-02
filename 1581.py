n = int(input())

for casos_testes in range(n):
    numero_pessoas = int(input())

    lista_idiomas = []

    for idioma_pessoas in range(numero_pessoas):
        idioma = str(input())
        lista_idiomas.append(idioma)

    todos_iguais = True
    primeiro_idioma = lista_idiomas[0]
    
    for idioma in lista_idiomas:
        if idioma != primeiro_idioma:
            todos_iguais = False
            break
    
    if todos_iguais:
        print(primeiro_idioma)
    else:
        print('ingles')