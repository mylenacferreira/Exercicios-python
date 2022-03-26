"""
Leia o peso de 5 pessoas e no final mostre qual foi o maior e o menor peso lido
"""
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite peso da {c} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} e o menor é {menor}')
