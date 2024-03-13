T = int(input())
A, B, C, D, E = map(int, input().split())

corretas = 0

if A == T:
    corretas += 1
if B == T:
    corretas += 1
if C == T:
    corretas += 1
if D == T:
    corretas += 1
if E == T:
    corretas += 1

print(corretas)