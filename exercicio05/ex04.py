'''Escreva um programa em Python que solicite ao usuário os valores de três contas deconsumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário ésuficiente para pagar as três contas, caso não seja apresente a mensagem “Salárioinsuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.'''

conta_luz = int(input("Informe o valor da conte de luz: "))
conta_agua = int(input("Informe o valor da conta de água: "))
conta_telefone = int(input("Informe o valor da conta de telefone: "))
salario = int(input("Digite o seu salário: "))
total_contas = conta_luz + conta_agua + conta_telefone
resto_salario =  salario - total_contas 

if total_contas > salario:
    print("Salário insuficiente!")
elif total_contas <= salario:
    print("Contas pagas!", "lhe restou ", "R$",resto_salario)
