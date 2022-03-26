"""
Calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no intervalo
de 1 ate 500

FORMA DE UTILIZAR MESMO PROCESSAMENTO
for cont in range(1, 501, 2)
"""

soma = 0
c = 0
for cont in range(1, 501):
    if cont % 2 == 1 and cont % 3 == 0:
        soma = soma + cont  # acumulador, recebe ele mesmo + proximo numero
        c = c + 1  # contador, recebe ele mesmo + 1
print(f'O somatório dos {c} numeros impares múltiplos de 3 é: {soma}')

