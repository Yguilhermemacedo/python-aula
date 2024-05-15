# inverte uma string

texto = input("Digite uma palavra: ")
textoInvertido = '' #varial auxiliar 

for letra in texto:
    textoInvertido = letra + textoInvertido
print(textoInvertido)

if textoInvertido == texto:
    print(f'{textoInvertido} é uma palímdrome.')
else:
    print(f'{textoInvertido} não é uma palímdrome.')