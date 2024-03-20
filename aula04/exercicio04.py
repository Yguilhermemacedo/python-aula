import math

# altura
h = float(input("Digite a altura da árvore: "))
bMenor = float(input("Digite a altura da base menor da  árvore: "))
bMaior = float(input("Digite a altura  da base maior da árvora: "))

volume = h/3*(bMaior**2 + bMenor**2 + (bMaior**2 * bMenor**2)**0.5)
print("O volume será: ", volume)