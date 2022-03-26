# faça um programa que calcule a média e avalie se foi aprovado, reprovado ou esta de recuperação

nota1 = float(input('Digite a sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média é: {media}. Situação: REPROVADO')
elif media > 7:
    print(f'Sua média é: {media}. Situação: APROVADO ')
else:
    print(f'Sua média é: {media}. Situação: RECUPERAÇÃO')
