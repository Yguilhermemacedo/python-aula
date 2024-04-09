'''Escreva um programa em Python que solicite ao usuário o valor da compra e o código referente a forma de pagamento. Calcule e mostre o valor a ser pago. Caso o código referente a forma de pagamento seja igual a 1, o algoritmo deve conceder 10% dedesconto, caso contrário 5%.'''

valor_compra = int(input("Digite o valor da compra: "))
forma_pagamento = int(input("Digite a forma de pagamento: 1,2,3: "))

if forma_pagamento == 1:
    print("Valor da compra: ", valor_compra - (valor_compra * 10 / 100))
else:
    print("Valor da compra: ", valor_compra - (valor_compra * 5 / 100))
