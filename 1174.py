A = list()

for i in range(0, 100):
    v = float(input())
    A.append(v)

for i in range(0, 100):
    if A[i] <= 10:
        print(f'A[{i}] = {A[i]:.1f}')
