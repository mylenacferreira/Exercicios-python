"""
Leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares , se o valor for impar
desconsidere-o
"""
soma = 0
for c in range(1, 7):
    ler = int(input(f'Digite o {c} numero: '))
    if ler % 2 == 0:
        soma = soma + ler
print(f'A soma dos números pares é {soma}')
