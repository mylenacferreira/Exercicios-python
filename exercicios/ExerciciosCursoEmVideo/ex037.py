# Receba um numero inteiro qualquer e peça para o usuario escolher base de conversão
# 1-binário 2-octal 3-hexa

num = int(input('Digite um número inteiro qualquer: '))
base = int(input('Digite qual a base de conversão desejada, sendo:\n1 - Binário\n2 - Octal\n3- Hexa: '))

if base == 1:
    print(f'{num} convertido para binário é {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para octal é {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Valor incorreto')