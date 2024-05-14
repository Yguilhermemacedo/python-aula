n = int(input("Digite um valor inteiro positivo para n: "))

if n >= 0:
    soma = 0
    for i in range(1, n+1):
        soma += 1/i
    print(f"A soma S = 1 + 1/2 + 1/3 + ... + 1/{n} é: {soma:.1f}")
else:
    print('Numero negativo não aceito!')
