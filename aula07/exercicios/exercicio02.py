n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
n3 = int(input("Digite outro número: "))

if n1 > n2 and n1 > n3:
    print(n1, " é o maior NÚMERO")
elif n2 > n1 and n2 > n3:
    print(n2," é o maior número.")
elif n3 > n1 and n3 > n2:
    print(n3, "é o maior número.")
else: 
    print("Número inválido!")