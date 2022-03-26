# Crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira
"""
Uma forma sem a importação da math seria
print(f'O numero {num} é um inteiro igual a {int(num)}')
"""
import math
num = float(input('Digite um numero qualquer: '))
print(f'O numero {num} é um inteiro igual a {math.trunc(num)}')
