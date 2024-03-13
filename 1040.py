n1, n2, n3, n4 = map(float, input().split())
nota = float(input())

peso1 = n1 * 2
peso2 = n2 * 3
peso3 = n3 * 4
peso4 = n4 * 1

media = (peso1 + peso2 + peso3 + peso4) /10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    print(f'Nota do exame: {nota:.1f}')
    
Recalculada_media = (nota + media) /2

if Recalculada_media >= 5.0:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')

print(f'Media final: {Recalculada_media:.1f}')