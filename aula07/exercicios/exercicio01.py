tipo_diaria = input("Informe  o tipo de diária.\n S para Simples\n D para Duplo\n T para Triplo: ")
qtd_diarias = int(input("Informe a quantidade de diarias desejadas: "))

if tipo_diaria == "S" or tipo_diaria =='s':
    print("Total das ",qtd_diarias, " será: ","R$", qtd_diarias * 225.50)
elif tipo_diaria == "D" or tipo_diaria == 'd':
    print("O valor total de ",qtd_diarias, " dias será de ","R$", qtd_diarias * 305.50)
elif  tipo_diaria == "T" or tipo_diaria =='t':
    print("O valor total de ",qtd_diarias, " dias será de ", "R$", qtd_diarias *360.50)
else:
    print("Tipo de diária inválida")