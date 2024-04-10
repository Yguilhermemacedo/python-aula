idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Não eleitoral.")
elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório.")
else:
    print("Eleitor facultativo")