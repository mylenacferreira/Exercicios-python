"""
Leia o ano de nascimento de 7 pessoas no final mostre quantas pessoas ainda não atingiram a maioridade e
quantas já sao maiores (considere 21 anos)
"""
from datetime import date
atual = date.today().year
cont = 0
cont1 = 0
for c in range(1, 8):
    nas = int(input('Digite o seu ano de nascimento: '))
    idade = atual - nas
    if idade >= 21:
        cont = cont + 1
    else:
        cont1 += + 1

print(f'{cont} pessoas atingiram a maioridade')
print(f'{cont1} pessoas ainda não atingiram a maioridade')
