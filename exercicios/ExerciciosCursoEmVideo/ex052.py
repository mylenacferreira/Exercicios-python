"""
Leia um numero inteiro e diga se ele é ou nao primo
"""
primo = int(input('Digite um numero inteiro qualquer: '))
cont = 0
for c in range(1, primo+1):
    if primo % c == 0:
        cont = cont + 1

if cont == 2:
    print(f'É primo pois o número {primo} foi divido {cont} vezes')
else:
    print(f'Não é primo pois o número {primo} foi divisível {cont} vezes')
