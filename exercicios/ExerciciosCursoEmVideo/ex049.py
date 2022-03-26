"""
Mostre a tabuada de um numero que o usuario escolher utilizando laço for
"""
n = int(input('Digite um numero inteiro de 1 a 10 para saber sua tabuada: '))
for c in range(0, 11):
    print(f'{n} x {c} = {c*n}')
