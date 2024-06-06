n = int(input())

tot_cobaias = tot_coelhos = tot_ratos = tot_sapos =  0

for c in range(n):
    q, t = (input()).split()
    q = int(q)
    if 1 <= q <= 15:
        tot_cobaias += q
        if t == 'C':
            tot_coelhos += q
        elif t == 'R':
            tot_ratos += q
        elif t == 'S':
            tot_sapos += q


print("Total: {} cobaias".format(tot_cobaias))
print("Total de coelhos: {}".format(tot_coelhos))
print("Total de ratos: {}".format(tot_ratos))
print("Total de sapos: {}".format(tot_sapos))

percentual_coelhos = (tot_coelhos / tot_cobaias) * 100
percentual_ratos = (tot_ratos / tot_cobaias) * 100
percentual_sapos = (tot_sapos / tot_cobaias) * 100

print("Percentual de coelhos: {:.2f} %".format(percentual_coelhos))
print("Percentual de ratos: {:.2f} %".format(percentual_ratos))
print("Percentual de sapos: {:.2f} %".format(percentual_sapos))