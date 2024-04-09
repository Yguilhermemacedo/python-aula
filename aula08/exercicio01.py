# entrada de dados 
compra = float(input('Digite o valor da compra: '))
parcelas = int(input("Digite a quantidade de parcelas: "))

# valor inicial da variável juros
juros = -1

# se a quantidade de parcelas for verdadeira (2,4,6,8) a variável juros será modificada
if parcelas == 2:
    juros = 3
elif parcelas == 4:
    juros == 7
elif parcelas == 6:
    juros == 9
elif parcelas == 8:
    juros = 12
else:
    print("Opção inválida!")

if juros != -1:
    parcela = (compra+compra*juros/100)/parcelas
    print("Valor da parcela: ", parcela)

# se a quantidade de parcelas for diferente, a variável juros não será modificada
else:
    print("Quantidade de parcelas inválida!")