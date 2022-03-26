# Verificar se 3 retas formam um triangulo e qual o tipo de triangulo

reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('É possível fazer um triangulo.', end=' ')
    if reta1 == reta2 == reta3:
        print('Equilátero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('NÃO é possível fazer um triangulo')
