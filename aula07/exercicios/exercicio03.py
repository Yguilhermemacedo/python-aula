peso = int(input("Informe seu peso: "))
altura = float(input('Informe sua altura: '))
imc = (peso / (altura ** 2))

if imc < 20:
    print("Você esta abaixo do peso.")
elif imc >= 20 and imc <25:
    print("Peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você esta em sobrepeso.")
elif imc >= 30 and imc < 40:
    print("Você esta obeso.")
else:
    print("Obeso Mórbido")

