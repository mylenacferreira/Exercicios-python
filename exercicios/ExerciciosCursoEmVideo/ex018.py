# Faça um programa que leia um angulo e mostre o valor do seno, cosseno e tangente

import math
ang = float(input('Digite um valor de ângulo qualquer: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo {} possui seno igual a {:.2f}\nCosseno igual a {:.2f}\nTangente igual a {:.2f}'.format(ang, seno, cosseno, tan))
