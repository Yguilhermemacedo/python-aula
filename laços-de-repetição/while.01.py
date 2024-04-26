r = 'S'
nao = 0
while r == 'S':
    respN = input('Quer cagar? [S/N]: ')
    if respN == 'S':
        nao = nao + 1
        r = str(input('Quer continuar? [S/N]: ')).upper()
    elif r == 'N':
        print(f'Voce negou {nao} vezes.')
print('Fim')