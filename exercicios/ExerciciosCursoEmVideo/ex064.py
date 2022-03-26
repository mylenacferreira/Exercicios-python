"""
Leia varios numeros inteiros e só pare quando o usuario digitar 999, no final mostre quantos numeros foram digitados
e qual foi a soma entre eles, desconsiderando o flag
"""
cont = 0
soma = 0
n = int(input('Digite um número, se quiser parar digite 999: '))
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite um número, se quiser parar digite 999: '))
print(f'O usuário digitou {cont} números e a soma de todos é {soma}')
