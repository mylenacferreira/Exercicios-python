"""
Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla, mostre e listagem e indique o maior e
o menor valor
"""
from random import randint
maior = menor = aux = 0
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'A listagem de numeros é: {tupla}')
print(f'O maior deles é {max(tupla)}')
print(f'O menor deles é {min(tupla)}')
