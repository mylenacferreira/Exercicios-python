"""
Leia o primeiro termo e a razao de uma progressao aritmética no final mostre os 10 primeiros termos
dessa PA
"""

primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU')
