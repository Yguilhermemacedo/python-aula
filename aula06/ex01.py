'''Escreva um programa em Python que solicite ao usuário o valor do denominador de uma fração, caso seja negativo mostre “valor inválido”'''

valor_denominador = int(input("Digite o primeiro valor: "))

if valor_denominador <= 0:
    print("Valor inválido")
else: 
    print("Valor correto!")