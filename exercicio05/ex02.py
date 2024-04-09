'''Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade dehoras trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas aseguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize umcaractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$37,50'''

turno = input("Informe o seu turno de trabalho: ")
horas = int(input("Informe a carga horária trabalhada: "))

if turno == "Manhã" or turno  == "manhã":
    print("Suas horas trabalhadas são de: ", horas * 45, " reais.")
elif turno == "Tarde" or turno  == "tarde":
    print("Sua hora trabalhada é de: ", horas * 37.50, " reais.")
elif  turno == "Noite" or turno == "noite":
    print("Sua horas trabalhadas são de: ", horas * 37.50, " reais.")
else:
        print("Turno inválido!")