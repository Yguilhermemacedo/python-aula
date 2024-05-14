
numero_decimal = int(input("Digite um número decimal: "))
base = int(input("Digite a base em que você deseja converter\n 1 [BINÁRIO]\n 2 [OCTAL]\n 3 [HEXADECIMAL]\n Digite a base: "))
print('=' *100)

binario = ''
octal = ''
hexadecimal = ''


        # Conversão de Decimal para Binário
if base == 1:
   dividendo = numero_decimal
   quociente = 1
   digitos = []
   while quociente >= 1:
      quociente = dividendo // 2
      resto = dividendo % 2
      digitos.insert(0,resto)
      dividendo = quociente 
      binario = "".join(str(digito) for digito in digitos)
print(f'O número {numero_decimal} [DECIMAL] convertido em Binário será: {binario}')

        # Conversão de Decimal para Octal
elif base == 2:
    dividendo = numero_decimal
    quociente = 1
    lista = []
    while quociente >= 1:
      quociente = dividendo // 8
      resto = dividendo % 8
      lista.insert(0,resto)
      dividendo = quociente 
      octal = "".join(str(item) for item in lista)
print(f'O número {numero_decimal} [DECIMAL] convertido em Binário será: {octal}')
    

elif base == 3:
    digitos = []
    while numero_decimal > 0:
       
        resto = numero_decimal % 16
        # Converte o resto para a letra hexadecimal correspondente
        if resto > 9:
            resto += 55  # Ajusta o valor para usar letras maiúsculas
            resto = chr(resto)
        digitos.insert(0, resto)
        numero_decimal //= 16
else:
    print('Erro.')