# faça um programa que leia os tres primeiros numeros e mostre qual é o maior e qual é o menor

num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Terceito numero: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é: {num1}')
    if num2 < num3:
        print(f'O menor número é: {num2}')
    else:
        print(f'O menor número é: {num3}')

elif num2 > num1 and num2 > num3:
    print(f'O maior numero é: {num2}')
    if num1 < num3:
        print(f'O menor número é: {num1}')
    else:
        print(f'O menor número é: {num3}')

else:
    print(f'O maior número é: {num3}')
    if num1 < num2:
        print(f'O menor número é {num1}')
    else:
        print(f'O menor número é: {num2}')
