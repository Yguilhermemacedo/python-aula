somai = 0 #acumulador
conti = 0 #contador

somas = 0 #acumulador
conts = 0 #contador

qtde = 0 #contador

while True:
    idade = int(input("Digite sua idade: "))
    salario = int(input("Digite o seu salario: "))

    if idade < 0:
        break

    somai = somai + idade
    conti = conti + 1

    if idade >= 40:
        somas = somas + salario
        conts = conts + 1
    if salario < 2000:
        qtde = qtde + 1

if somai > 0:
    media = somai/conti

    medias = somas/conts

    print('Média das idades: ', media)
    print("Salário média das pessoas com >= 40: ", medias)
    print('Quantidade de pessoas com salario < 2000')