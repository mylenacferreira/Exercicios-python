# Ano de nascimento e calcule sua idade para se enquadrar na sua categoria
from datetime import date
ano = int(input('Digite qual o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Você tem {idade} anos.')

if idade < 9:
    print('Categoria: MIRIM')
elif 9 <= idade < 14:
    print('Categoria: INFANTIL')
elif 14 <= idade < 19:
    print('Categoria: JUNIOR')
elif 19 <= idade < 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
