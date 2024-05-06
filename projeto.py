
numero_decimal = int(input("Digite um número decimal: "))

def decimal_para_hexadecimal(numero_decimal):

  while numero_decimal > 0:
    digitos = []
    resto = numero_decimal % 16
    # Converte o resto para a letra hexadecimal correspondente
    if resto > 9:
      resto += 55  # Ajusta o valor para usar letras maiúsculas
      resto = chr(resto)
    digitos.insert(0, resto)
    numero_decimal //= 16

  # Junta os dígitos hexadecimais em uma string
  hexadecimal = "".join(str(digito) for digito in digitos)
  
  return hexadecimal
hexadecimal = decimal_para_hexadecimal(numero_decimal)
print(f"O número {numero_decimal} em hexadecimal é: {hexadecimal}")




