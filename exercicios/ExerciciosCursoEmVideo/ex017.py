# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# e calcule sua hipotenusa
"""
Maneira matematica
hip = (oposto ** 2 + adj ** 2) ** (1/2)

from math import hypoy
nesse caso para realizar a conta não precisa so math.hypot, apenas de hypot
"""
import math
oposto = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O comprimento da hipotesuna deste triângulo retângulo é de {math.hypot(oposto, adj)}')
