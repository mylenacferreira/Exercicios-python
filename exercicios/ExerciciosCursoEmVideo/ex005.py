# Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor

numero = int(input('Digite um numero inteiro: '))
sucessor = numero + 1
antecessor = numero - 1
print('O sucessor de {} é {} e o seu antecessor é {}' .format(numero, sucessor, antecessor))
'''
Para não precisar criar variaveis novas
print('O sucessor de {} é {} e o seu antecessor é {}' .format(numero, (numero+1), (numero-1)))
'''
