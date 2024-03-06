p1, np1, vu1 = map(float, input().split())
p2, np2, vu2 = map(float, input().split())


valorpago = np1 * vu1 + np2 * vu2

print (f'VALOR A PAGAR: R$ {valorpago:.2f}')

