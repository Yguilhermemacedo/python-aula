n = int(input('Digite um número positivo: '))

if n >=0:
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i
        print(int(soma))
else:
    print(f'Erro! O número {n} digitado é negativo. Tente novamente com números POSITIVOS.')