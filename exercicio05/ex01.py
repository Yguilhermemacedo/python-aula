'''Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valorentre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”.'''

num = int(input("Digite um número: "))
if num <= 9:
    print(num, " valor correto!")
else :
    print("Número incorreto!")