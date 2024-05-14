num_valores = int(input("Digite o número de valores que deseja inserir: "))

positivos = 0
negativos = 0
menor_valor = float('inf')  # Inicializa o menor valor com infinito positivo

for i in range(num_valores):
    valor = float(input(f"Digite o valor {i+1}: "))
    
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    
    # Atualiza o menor valor
    if valor < menor_valor:
        menor_valor = valor

print(f"Número de valores positivos: {positivos}")
print(f"Número de valores negativos: {negativos}")
print(f"O menor valor é: {menor_valor}")