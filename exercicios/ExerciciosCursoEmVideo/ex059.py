"""
Leia dois valores e faça
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
realize a operação
"""

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('O que deseja fazer com esses valores, sendo \n[1] - somar\n'
                     '[2] - multiplicar\n[3] - maior\n[4] - novos numeros\n[5] - sair do programa: '))
    if menu == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}')
    elif menu == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif menu == 3:
        if num1 > num2:
            print(f'O número {num1} é o maior')
        elif num1 == num2:
            print('Os números são iguais')
        else:
            print(f'o número {num2} é maior')
    elif menu == 4:
        num1 = int(input('Digite novamente o primeiro valor: '))
        num2 = int(input('Digite novamente o segundo valor: '))
    elif menu > 5:
        print('Opção inválida')
print('FIM')
