# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"

cid = str(input('Digite o nome da sua cidade: ')).strip()

print(cid[:5].upper() == 'SANTO')

# Jogou todo nome para maíusculo e verificou se é santo, entao mesmo digitando "errado" será True
