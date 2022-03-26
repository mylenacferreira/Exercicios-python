"""
Leia um numero n inteiro e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci
"""
n = int(input('Digite a quantidade de elementos de uma sequencia Fibonacci: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
