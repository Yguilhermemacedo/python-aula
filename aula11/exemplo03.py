numeros = []
soma = 0
qtde = 0
while True:
    numero = int(input('Digite  um número: '))

    if numero == 0:
        break

    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)


for numero in numeros:
    if numero > media:
        qtde = qtde + 1

print(f'Media: {media:.2f}')
print(f'Acima da média: {qtde}')