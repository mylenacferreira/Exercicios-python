"""
Crie uma tupla totalmente preenchida com uma contagem por extenso de zero ate vinte. Deverá ler um numero do teclado
e apresenta-lo por extenso
"""

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
usu = int(input('Digite um número de 0 a 20: '))
while usu > 20 or usu < 0:
    usu = int(input('Número incorreto. Digite novamente: '))
cont = usu
print(f'Você digitou {n[cont]}')
