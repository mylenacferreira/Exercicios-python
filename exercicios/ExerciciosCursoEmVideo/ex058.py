"""
Computador vai pensar um numero de 0 ate 10, o jogador vai tentar adivinhar ate acertar mostrando no final
quantos palpites foram necessários
"""

from random import randint
cont = 1
comp = randint(0, 10)
jog = int(input('Digite um número de 0 a 10 para jogo da adivinhação: '))

while jog != comp:
    jog = int(input(f'Errou! Tente novamente: '))
    if jog == comp:
        print(f'Ganhou! Computador escolheu {comp} e você também escolheu {jog}')
    cont += 1
print(f'Foram necessários {cont} palpites para você vencer.')
