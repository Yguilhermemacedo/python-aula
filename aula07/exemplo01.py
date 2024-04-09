# entrada de dados
media = float(input("Digite sua média: "))
f = float(input("Informe sua porcentagem de frequência: "))

# condições compostas
if f <= 75:
    print("Reprovado por faltas!")
elif media < 6:
    print("Reprovado por nota.")
else:
    print("Aprovado!")