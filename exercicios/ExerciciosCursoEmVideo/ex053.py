"""
Leia uma frase qualquer e diga se ela é um palíndromo

UMA FORMA SEM O FOR
inverso = junto[::-1]
"""
frase = str(input('Digite uma frase qualquer: ')).strip()
div = frase.split()
junto = ''.join(div) # junção das palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("É um palíndromo")
else:
    print('Não é um palíndromo')