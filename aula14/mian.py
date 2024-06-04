import metodos
import math

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = metodos.calcula_imc(peso, altura)
print(imc)

