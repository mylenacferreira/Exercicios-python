# Escreva um programa que faça o computador "pensar" em um numero inteiro de 0 a 5. Tente descobrir qual numero
# escolhido pelo computador.
"""
Outra forma de fazer
num = random.randint (0, 5)
O comando sleep vai fazer o computador "descansar" por (3) segundos
"""

import random
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
num = random.choice(lista)
print('Olá, tente adivinhar qual numero eu estou pensando, entre 0 e 5')
chute = int(input('Digite qual número você acredita que eu tenha escolhido: '))
print('Processando...')
sleep(3)
if chute == num:
    print(f'Você ganhou, eu escolhi {num} e você {chute}')
else:
    print(f'Você perdeu, eu escolhi {num} e você {chute}')
