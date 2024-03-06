valor = int(input())

print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

quantidade_notas_100 = valor // 100
valor %= 100

quantidade_notas_50 = valor // 50
valor %= 50

quantidade_notas_20 = valor // 20
valor %= 20

quantidade_notas_10 = valor // 10
valor %= 10

quantidade_notas_5 = valor // 5
valor %= 5

quantidade_notas_2 = valor // 2
valor %= 2

quantidade_notas_1 = valor

print(quantidade_notas_100, "nota(s) de R$ 100,00")
print(quantidade_notas_50, "nota(s) de R$ 50,00")
print(quantidade_notas_20, "nota(s) de R$ 20,00")
print(quantidade_notas_10, "nota(s) de R$ 10,00")
print(quantidade_notas_5, "nota(s) de R$ 5,00")
print(quantidade_notas_2, "nota(s) de R$ 2,00")
print(quantidade_notas_1, "nota(s) de R$ 1,00")