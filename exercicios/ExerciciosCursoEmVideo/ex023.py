# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos sepados

num = int(input('Digite um numero qualquer de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')

"""
if tam == 4:
    unidade = num[3]
    dezena = num[2]
    centena = num[1]
    milhar = num[0]
    print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')
elif tam == 3:
    unidade = num[2]
    dezena = num[1]
    centena = num[0]
    print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}')
elif tam == 2:
    unidade = num[1]
    dezena = num[0]
    print(f'Unidade: {unidade}\nDezena: {dezena}')
else:
    unidade = num[0]
    print(f'Unidade: {unidade}')

"""