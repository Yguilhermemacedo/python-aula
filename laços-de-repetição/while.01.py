base_convertida = int(input('Digite qual base será convertida\n 1 - Decimal\n 2 - Hexadecimal\n 3 - Binário\n Insira a base que será convertida:'))
base = int(input('Digite qual base você deseja\n 1 - Binário\n 2 - Decimal\n 3 - Hexadecimal\n Digite base:'))

if base_convertida == 1 and base == 1:
    dividendo = int(input("Digite um número (Base decimal) para ser convertido em Binário: "))
    numero_digitado = dividendo
    quociente = 1
    lista = []
    while quociente >= 1:
       quociente = dividendo // 2
       resto = dividendo % 2
       lista.insert(0, resto)
       dividendo = quociente
       binario = ''.join([str(item) for item in lista])
    print("O número", numero_digitado, " convertido em binário será:", binario)
else:
    print('Erro.')