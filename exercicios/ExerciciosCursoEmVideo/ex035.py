# Verificar se 3 retas formam um triangulo

reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
        print('É possível fazer um triangulo.')
else:
        print('NÃO é possível fazer um triangulo')
