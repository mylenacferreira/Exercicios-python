# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Digite um numero de 1 a 10 para calcular sua tabuada: '))
print(f' {num} x 0 = 0\n {num} x 1 = {num}\n {num} x 2 = {num * 2}\n {num} x 3 = {num * 3}\n {num} x 4 = {num * 4}\n {num} x 5 = {num * 5}\n {num} x 6 = {num * 6}\n {num} x 7 = {num * 7}\n {num} x 8 = {num * 8}\n {num} x 9 = {num * 9}\n {num} x 10 = {num * 10}\n')

"""
outra forma de fazer
print('{} x {} = {}' .format(num, 1, num*1))
print('{} x {} = {}' .format(num, 2, num*2))
"""