# Crie um programa para receber qualquer coisa do usuario e mostre seu tipo
n = input('Digite algo ')
print('O tipo primitivo desse valor é: ', type(n))
print('É somente espaços? ', n.isspace())
print('É um numero? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Esta em letras maiusculas? ', n.isupper())
print('Esta em letras minusculas? ', n.islower())
print('Esta capitalizada? ', n.istitle())  # somente com primeira letra maiuscula

"""
Nesse caso n é o que chamamos de objeto, ou seja, possui caracteristicas e realiza funcionalidades então
ele tem atributos e metodos. Todo objeto string possui metodos
"""