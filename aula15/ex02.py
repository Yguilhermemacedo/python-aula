'''Construir um método em Python que receba como parâmetros o valor de uma
compra e a quantidade de parcelas e calcula e retorna o valor da parcela, sabendo que
a loja acrescenta 5% de juros para as compras parceladas.
No programa principal, solicite para o usuário o valor de uma compra e a quantidade
de parcelas e utilizando o método descrito acima, mostre o valor da parcela.'''

def parcelas(valor_compra, qte_parcelas):
    valor_parcelas = (valor_compra + (valor_compra*5/100))/ qte_parcelas
    total = valor_parcelas
    return total
    
valor_compra = float(input('Qual o valor da compra? : '))
qte_parcelas = int(input('Qual a quantidade de parcelas: '))
print(f'O valor das parcelas será: {parcelas(valor_compra,qte_parcelas)}',)