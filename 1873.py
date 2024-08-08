c = int(input())
for casos_testes in range(c):
    m, n = input().split(' ')
    if m == 'tesoura' and n == 'papel':
        print('rajesh')
    elif m == 'papel' and n == 'pedra':
        print('rajesh')
    elif m == 'pedra' and n == 'lagarto':
        print('rajesh')
    elif m == 'lagarto' and n == 'spock':
        print('rajesh')
    elif m == 'spock' and n == 'tesoura':
        print('rajesh')
    elif m == 'tesoura' and n == 'lagarto':
        print('rajesh')
    elif m == 'lagarto' and n == 'papel':
        print('rajesh')
    elif m == 'papel' and n == 'spock':
        print('rajesh')
    elif m == 'spock' and n == 'pedra':
        print('rajesh')
    elif m == 'pedra' and n == 'tesoura':
        print('rajesh')
    
    if m == 'papel' and n == 'tesoura':
        print('sheldon')
    elif m == 'pedra' and n == 'papel':
        print('sheldon')
    elif m == 'lagarto' and n == 'pedra':
        print('sheldon')
    elif m == 'spock' and n == 'pedra':
        print('sheldon')
    elif m == 'tesoura' and n == 'spock':
        print('sheldon')
    elif m == 'lagarto' and n == 'tesoura':
        print('sheldon')
    elif m == 'papel' and n == 'lagarto':
        print('sheldon')
    elif m == 'spock' and n == 'papel':
        print('sheldon')
    elif m == 'pedra' and n == 'spock':
        print('sheldon')
    elif m == 'tesoura' and n == 'pedra':
        print('sheldon')

    if m == 'tesoura' and n == 'tesoura':
        print('empate')
    elif m == 'pedra' and n == 'pedra':
        print('empate')
    elif m == 'papel' and n == 'papel':
        print('empate')
    elif m == 'lagarto' and n == 'lagarto':
        print('empate')
    elif m == 'spock' and n == 'spock':
        print('empate')