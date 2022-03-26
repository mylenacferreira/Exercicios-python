"""
Leia varios numeros inteiros e só pare quando o usuario quiser, no final mostre a media de todos e qual foi o
maior e menor valor
"""

n = 0
cont = soma = total = maior = menor = 0
r = 'n'
while r == 'n':
    n = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja parar? [S/N]: ')).lower()
total = soma / cont
print(f'O usuário digitou {cont} números e a média de todos é {total}')
print(f'O maior valor digitado foi {maior} e o menor {menor}')