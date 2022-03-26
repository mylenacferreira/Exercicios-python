# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um numero: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O dobro de {} é {}, \nO triplo é {} \nE sua raiz quadrada é {:.2f}' .format(num, dobro, triplo, raiz))

# Da mesma forma que o anterior, pode fazer a conta dentro do format
# raiz quadrada pode ser feita de pow(num, (1/2))
