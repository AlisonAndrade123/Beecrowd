pares = 0
impar = 0
positivo = 0
negativo = 0

for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
    if valor % 2 == 1:
        impar += 1
    if valor > 0:
        positivo += 1
    if valor < 0:
        negativo += 1

print(pares, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
