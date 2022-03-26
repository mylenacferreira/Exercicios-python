# Receba dois numeros inteiros e compare-os, mostre na tela o primeiro valor é maior, o segundo
# valor é maior ou não existe valor maior, são iguais

num1 = int(input('Digite um número inteiro qualquer: '))
num2 = int(input('Digitr mais um número inteiro qualquer: '))

if num1 == num2:
    print('Não existe número maior pois ambos são iguais.')
elif num1 > num2:
    print(f'O primeiro número é maior: {num1} > {num2}')
else:
    print(f'O segundo número é o maior: {num2} > {num1}')
