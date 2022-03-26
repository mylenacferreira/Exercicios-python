"""
Crie um programa que leio o come completo de uma pessoa e mostre.
1 - O nome com todas as letras maisculas
2 - O nome com todas as letras minúsculas
3 - Quantas letras ao todo, sem considerar espaços
4 - Quantas letras tem o primeiro nome
"""

nome = str(input('Digite seu nome completo: ')).strip()  # Strip para tirar espaços desnecessários
print(f'O seu nome completo maiúsculo é: {nome.upper()}')
print(f'O seu nome completo minúsculo é: {nome.lower()}')
div = nome.split()
print('O seu nome completo possui {} caracteres'.format(len(nome) - nome.count(' ')))
print(f'O seu primeiro nome é {div[0]} e possui {len(div[0])} letras')

# Na lógica do 3 é somar o nome completo e subtrair da somatória dos espaços
