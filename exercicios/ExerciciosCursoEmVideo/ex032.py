# faça um programa que leia um ano qualquer e diga se é ou não bissexto

from datetime import date
data = int(input('Digite um ano qualquer. Coloque 0 para analisar o ano atual:  '))
if data == 0:
    data = date.today().year

if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print(f'O ano de {data} é Bissexto')
else:
    print(f'O ano de {data} não é Bissexto')
