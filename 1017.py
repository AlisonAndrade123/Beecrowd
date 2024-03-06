gasto_horas = int(input())
velocidade_media= int(input())

distancia = gasto_horas * velocidade_media

litros_necessarios = distancia / 12


print (f'{litros_necessarios:.3f}')