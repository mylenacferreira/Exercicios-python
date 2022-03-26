tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Voce digitou {tupla}')
print(f'O numero 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'A posição do numéro 3 é: {tupla.index(3)+1}')
else:
    print('O valor 3 não apareceu')
print('Os numeros pares são: ')
for n in tupla:
    if n % 2 == 0:
        print(f'{n} ', end='')
