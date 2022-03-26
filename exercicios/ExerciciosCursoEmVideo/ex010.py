# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto ela pode comprar em dolar

din = float(input('Digite quantos reais você tem na carteira: R$'))
dol = din / 3.27
print('Com R${:.2f} você pode comprar ${:0.2f} '.format(din, dol))
