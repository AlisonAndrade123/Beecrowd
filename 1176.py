def calcula_fibonacci():
    fibonacci = [0, 1]
    for i in range(2, 61):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci

T = int(input())

fibonacci = calcula_fibonacci()

for i in range(T):
    N = int(input())
    print(f"Fib({N}) = {fibonacci[N]}")
