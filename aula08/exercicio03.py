nome_produto = print(input("Informe o nome do produto: "))
valor_compra = float(input("Digite o valor da venda: "))

lucro = -1

if valor_compra < 10:
    lucro = 70
elif valor_compra <= 10 and  valor_compra < 30:
    lucro = 50
elif valor_compra <= 30 and valor_compra < 50:
    lucro = 40
else:
    lucro  = 30
    venda = valor_compra + (valor_compra * (lucro / 100.0))
    print("\nProduto: ", nome_produto)
    print("Valor de Compra: R$",valor_compra)
