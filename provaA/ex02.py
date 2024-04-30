mes = int(input('Digite o mês da viagem: '))
passagens = int(input('Digite a quantidade de passagens desejada: '))

if passagens >= 0 and mes < 12:
    if mes >= 2 and mes <=5:
        valor = passagens * 350.99
        print(f"Foram escolhidas {passagens} passagens, o valor total das passagens será de:R${valor}")  
    elif mes == 1 or mes == 6 or mes == 7 or mes == 12:
        valor = passagens * 520.50
        print(f"Foram escolhidas {passagens}, o valor total das será de:R${valor}")
    elif mes == 8 or mes == 9 or mes == 10 or mes == 11:
        valor = passagens * 450.75
        print(f"Foram escolhidas {passagens}, o valor total das será de:R${valor}")
elif mes > 12:
    print('Mês inválido.')
else:
     print('Quantidade de passagens inválidas.')