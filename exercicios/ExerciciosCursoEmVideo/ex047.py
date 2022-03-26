"""
Mostre na tela todos os numeros pares que estão entre 1 e 50
"""

soma = 0
for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont)
        soma += cont
print(f'O somátorio dos numeros pares entre 1 e 50 é {soma}')

"""
Uma forma de utilizar menos o processador do pc é fazer
for cont in range(2, 51, 2)
"""