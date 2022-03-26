# Escreva um programa que leia um valor em metros e o exiba converido em centimentros e milimetros

metro = float(input('Digite o valor em metros: '))
cent = metro * 100
mili = metro * 1000
print(f'{metro} metros equivale a {cent} centimetros e {mili} milímetros')
