num = int(input("Digite um número com três dígitos: "))
# Primeiro dígito
d1 = num // 100
print("Primeiro dígito: ", d1)
d2 = num % 100 // 10
print("Segundo dígito: ", d2)
d3  = num % 10
print("Terceiro dígito:" , d3)
inverso = d3 * 100 + d2 * 10 +d1
print("Inversão do número:", inverso)
