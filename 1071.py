X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

soma_impares = 0


for i in range(X+1, Y):
    
    if i % 2 != 0:
        soma_impares += i

print(soma_impares)
