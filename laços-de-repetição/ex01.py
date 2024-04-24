# i = int(input("Início: ")) #lendo o início
# f = int(input('Fim: ')) #lendo o fim
# p = int(input('Passo: ')) #lendo o passo

# #irá começar com o número indicado na variável 'i' 
# #onde irá terminar, indicado com a variável 'f'
# #e quantos passos irá contar com o valor 'p'
# for c in range(i, f+1, p):
#     print(c)
# print('FiM!')

passo = int(input("Qunatos passos?: "))
pulos = int(input('Informe a quantidade de pulos: '))
for c in range(passo, pulos):
    print(f'Passo {c}')
    print(f'Pulo {pulos}')
    print(c)
print(f'Você chegou ao seu destino com {passo} passos, e {pulos} pulos.')