'''Uma empresa está selecionando entre seus estagiários os que irão fazer um treinamento especial. O selecionado deve satisfazer ao mesmo tempo a dois critérios.O primeiro critério é que ele deve ter uma bolsa maior ou igual a R$ 750,00 e menor ouigual a R$ 950,00.O segundo critério leva em conta o tempo de estágio, este deve ser maior ou igual a 2 anos.'''

valor_bolsa = int(input("Informe o valor da bolsa: "))
tempo_estagio = int(input("Informe o tempo de estágio: ")) 

if valor_bolsa >= 750 and valor_bolsa <= 950 and tempo_estagio >= 2:
    print("Participará do treinamento!")
else:
    print("Não participará do treinamento!")