"""
Leia o primeiro termo e a razao de uma progressao aritmética no final mostre os 10 primeiros termos
dessa PA
"""
primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
termo = primeiro
cont = 0
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont = cont + 1
print('Fim')