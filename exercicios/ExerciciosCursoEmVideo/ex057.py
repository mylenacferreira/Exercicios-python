"""
Leia o sexo de uma pessoa mas so aceite M ou F. Caso esteja errado peça a digitação novamente ate ter
um valor correto
"""
sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido, digite novamente seu sexo [M/F]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso')
