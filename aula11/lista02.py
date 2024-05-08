nomes = list()

for i in range(5):
    n = input('Digite o nome: ')
    nomes.insert(i, n)

for nome in range(len(nomes)):
    print(nomes[nome])    

# ordem alfabética usando o método sort()
nomes.sort()
print(nomes)
# ordem inversa usando o método reverse()
nomes.reverse()
print(nomes)