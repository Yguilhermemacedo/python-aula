'''Escreva um programa em Python que solicite a entrada de 2 notas de alunos e exiba qual é a maior (desconsidere notas iguais).'''

n1_aluno1 = float(input("Digite a primeira nota do aluno 1: "))
n2_aluno1 = float(input("Digite a segunda nota do aluno 1: "))
media_aluno1 = n1_aluno1  + n2_aluno1 / 2

n1_aluno2 = float(input("Digite a primeira nota do aluno 2: "))
n2_aluno2 = float(input("Digite a segunda nota do aluno 2: "))
media_aluno2 = n1_aluno2 + n2_aluno2 / 2

if  media_aluno1 > media_aluno2:   
    print ("O aluno com a média mais alta é de ", media_aluno1, "o Aluno 1")
elif media_aluno2 > media_aluno1:
    print("O aluno que obteve a melhor média foi o Aluno 2", " com", media_aluno2)
else:
    print("São iguais!")


