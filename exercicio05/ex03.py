'''Faça um programa em Python que obtenha o valor de uma compra, calcular e mostrar o valor da compra considerando o desconto, conforme descrito abaixo:para compras acima de R$ 200 a loja dá um desconto de 20% para as abaixo disso não tem desconto, mostre o valor da compra'''

valor_compra = int(input("Informe o valor total da compra: "))
desconto = valor_compra / 100 *20

if valor_compra > 200:
    print("O valor total da compra é de ", "R$",valor_compra, " e com os 20% de desconto, o valor será de: ", "R$", desconto)
else:
    print("O valor da compra será: ", "R$",valor_compra)
