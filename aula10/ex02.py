resp = 's'

while resp.upper() == "S":
    h = float(input("Digite sua altura: "))
    sexo = input("Digite M - Masculino ou F - Feminino: ")
    if sexo.upper() == 'M':
        peso_ideal = (72.7*h) - 58
    elif sexo.upper() == 'F':
        peso_ideal = (62.1*h) - 44.7
    else:
        peso_ideal = 0

    if peso_ideal != 0:
        print("Peso ideal = ", peso_ideal)
    else:
        print("Informação inválida.")
    #atualização da variável de controle
        resp = input("Deseja continuar? (s/n): ")