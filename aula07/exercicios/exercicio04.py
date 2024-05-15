'''Elabore um programa em Python que implemente uma calculadora com as funções de
somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
valores, e perguntar qual a operação pretendida (+, - , * ou / ) e a seguir calcular e
mostrar o resultado.'''

numero = int(input("Digite um número: "))
opcao = int(input('Escolha as operações que seja fazer\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n Escolha: '))

if opcao == 1:
    print("=" *100)
    print('OPERAÇÃO SOMA SELECIONADA')
    num2 = int(input(f'Deseja somar {numero} por: '))
    res = numero + num2
    print(f'A soma entre {numero} e {num2} é igual: {res}')
elif opcao == 2:
    print("=" *100)
    print('OPERAÇÃO SUBTRAIR SELECIONADA')
    num2 = int(input(f'Deseja subtrair {numero} por: '))
    res = numero - num2
    print(f'A subtração entre {numero} e {num2} será: {res}')
elif opcao == 3:
    print("=" *100)
    print('OPERAÇÃO MULTIPLICAR SELECIONADA')
    num2 = int(input(f'Deseja multiplicar {numero} por: '))
    res = numero * num2
    print(f'{numero} multiplicado por {num2} será: {res}')
elif opcao == 4:
    print("=" *100)
    print('OPERAÇÃO DIVISÃO SELECIONADA')
    num2 = int(input(f"Deseja dividir {numero} por: "))
    res = numero // num2
    print(f'A divisão de {numero} por {num2} será: {res}')
else:
    print('Erro. Digite a operação desejada!')