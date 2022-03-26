# Leia um frase completa e mostre quantas veze aparece a letra a, em qual posiçao aparece pela 1 vez
# em qual posição aparece pela ultima vez

frase = str(input('Digite uma frase qualquer: ')).upper().strip()

print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)  # Começa da direita para esquerda
