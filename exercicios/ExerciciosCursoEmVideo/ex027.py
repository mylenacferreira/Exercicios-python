# Leia o nome completo de uma pessoa mostrando o se primeiro e ultimo nome separadamente

nome = str(input('Qual seu nome completo: ')).strip()
div = nome.split()
print(f'O seu primeiro nome é: {div[0]}')
print(f'O seu último nome é: {div[len(div)-1]}')

# vai contar quantas palavras tem -1, pois começa em 0