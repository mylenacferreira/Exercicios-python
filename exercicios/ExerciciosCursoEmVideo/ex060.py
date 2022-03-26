"""
Leia um número qualquer e mostre o seu fatorial
"""
num = int(input('Digite um numero qualquer: '))
cont = num
aux = 1
print(f'Calculando fatorial de {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    aux = aux * cont
    cont = cont - 1
print(f'{aux}')
