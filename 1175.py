N = []

for i in range(20):
    valor = int(input())
    N.append(valor)

for i in range(10):
    valor = N[i]
    N[i] = N[19 - i]
    N[19 - i] = valor

for i in range(20):
    print(f"N[{i}] = {N[i]}")