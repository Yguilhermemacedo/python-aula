'''Faça um método em Python que receba como parâmetros o Km inicial, Km final,
quantidade de litros gastos e preço do litro. Calcule e mostre:
- Distância percorrida;
- Consumo médio;
- Valor gasto;'''

def distancia(km_inicial, km_final, qtde_litros, preco_litro):
    km = (km_inicial - km_final)**2

km_inicial = int(input('Qual o Km incial? : '))
km_final = int(input('Qual o Km final? : '))
qtde_litros = int(input('Quantos litros de combústível: '))
preco_litro = int(input('Qual o preço do litro? : '))