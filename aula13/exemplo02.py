# função strip() - retira espaço antes e depois e quebra de linha

nome = input('Digite algo: ')
print(nome.strip()+ "Seja bem vindo")
print("de" in nome)

#metodo  find - retorna onde a substring começa na string
print(nome.find("me"))

#método replace - troca todas as ocorrências de uma string em uma string
print(nome.replace('r', 'l'))

# Lowercase e Uppercase

print(nome.upper())
print(nome.lower())

#split - divide a string de acordo com o caratcter - gera uma lista
n = nome.split(" ")
print(n)

#cont - retorna a quantidade de elementos de uma string
print(nome.count("a"))

print('Este é o seu nome sem nenhum espaço ',nome.strip())