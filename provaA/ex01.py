import math
x1 = int(input('Digite a primeira coordenada: '))
x2 = int(input("Digite a segunda coordenada: "))

y1 = int(input('Digite a terceira  coordenada: '))
y2  = int(input('Digite a quarta coordenada: '))

p1 = x1,y1
p2 =  x2,y2

d =float(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
print(f'A distância entre o P1({p1}) e o P2({p2}) é: {d}')