"""
Leia o primeiro termo e a razao de uma progressao aritmética no final mostre os 10 primeiros termos
dessa PA e pergunte ao usuario se deseja mais termos, programa finaliza quando usuario apertar 0
"""
primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont = cont + 1
    mais = int(input('Mais quantos termos deseja mostrar? '))
print(f'Fim com total de {total} termos')
