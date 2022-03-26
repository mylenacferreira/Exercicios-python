# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Qual o preço do produto? R$'))
desc = preco * 0.95
print('O produto custava R${}, com 5% de desconto, seu valor será R${:.2f}' .format(preco, desc))
