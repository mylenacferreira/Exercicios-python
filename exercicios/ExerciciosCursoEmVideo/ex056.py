"""
Leia o nome, a idade e o sexo de 4 pessoas e mostre
A media de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres tem menos de 20 anos
"""
media = 0
aux = 0
cont = 0
hnome = ''
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c} pessoa: ')).capitalize()
    idade = int(input(f'Digite a idade da {c} pessoa: '))
    sexo = str(input(f'Digite o sexo da {c} pessoa, (m ou f): ')).lower()
    media = media + idade
    if sexo == 'm':
        if idade > aux:
            aux = idade  # homem mais velho
            hnome = nome
    else:
        if idade < 20:
            cont = cont + 1

print(f'A média de idade do grupo é {media/4}')
print(f'O homem mais velho tem {aux} anos e se chama: {hnome} ')
print(f'Neste grupo há {cont} mulheres com menos de 20 anos')
