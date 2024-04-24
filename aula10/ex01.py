qtdeEleitores = 0
soma = 0
qtdeNEleitores = 0

for i in range(5):
    idade = int(input("Digite sua idade: "))
    if idade >= 16:
        qtdeEleitores = qtdeEleitores + 1
    else:
        qtdeNEleitores = qtdeNEleitores + 1
        soma = soma + idade

media = soma/qtdeNEleitores
print("Quantidade de eleitores ", qtdeEleitores)
print("Media de idade dos alunos não eleitores, ", media)