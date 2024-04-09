peso = int(input("Informe seu peso: "))
altura = float(input('Informe sua altura: '))
imc = (peso / (altura ** 2))

if imc < 20:
    print("%.2f você esta abaixo do peso." %)
elif imc >= 20 and imc <25:
    print("%.2f você está no peso ideal." %)
elif imc >= 25 and imc < 30:
    print("%.2f você esta em sobrepeso." %)
elif imc >= 30 and imc < 40:
    print("%.2f você esta obeso." %)
else:
    print("Obeso Mórbido")

