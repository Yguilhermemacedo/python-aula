nomes = [] # Criando lista

for i in range(5): # Coletando dados através da variável (n) 
    n = input('Digite um nome: ')
    nomes.insert(i, n)  # a função append() adiciona valores em lista

for x,e  in enumerate(nomes):
    print('[%d] - %s' %(x+1, e))
print(nomes)