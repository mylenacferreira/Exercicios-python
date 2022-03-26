# JOGO JOKENPÔ

import random
from time import sleep
jogador = str(input('Digite qual você quer: Pedra, Papel ou Tesoura: ')).lower()
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

if jogador == 'pedra' and computador == 'tesoura':
    print(f'Jogador:{jogador} X Computador: {computador}. JOGADOR GANHOU')
elif jogador == 'pedra' and computador == 'papel':
    print(f'Jogador:{jogador} X Computador: {computador}. COMPUTADOR GANHOU')
elif jogador == 'tesoura' and computador == 'papel':
    print(f'Jogador:{jogador} X Computador: {computador}. JOGADOR GANHOU')
elif jogador == 'tesoura' and computador == 'pedra':
    print(f'Jogador:{jogador} X Computador: {computador}. COMPUTADOR GANHOU')
elif jogador == 'papel' and computador == 'pedra':
    print(f'Jogador:{jogador} X Computador: {computador}. JOGADOR GANHOU')
elif jogador == 'papel' and computador == 'tesoura':
    print(f'Jogador:{jogador} X Computador: {computador}. COMPUTADOR GANHOU')
elif jogador == computador:
    print(f'Jogador:{jogador} X Computador: {computador}. EMPATE')
else:
    print('Jogada inválida')
