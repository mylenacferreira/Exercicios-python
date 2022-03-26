# Crie um programa que leia um numero inteiro e mostre na tela se é PAR ou IMPAR

num = int(input('Digite um número inteiro qualquer: '))
resto = num % 2

if resto == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é IMPAR ')
