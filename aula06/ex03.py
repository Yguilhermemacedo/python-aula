'''Escreva um programa em Python que solicite ao usuário dois números inteiros ele sempre realizará a subtração do maior pelo menor, não importando a ordem.'''

n1 = int(input('Informe um número: '))
n2 = int(input("Informe  outro número: "))

if n1 > n2:
    print("Subtração: ", (n1 - n2))
elif n2 > n1:
    print("Subtração: ", (n1 - n2))
else: 
    print("Os números são iguais.")