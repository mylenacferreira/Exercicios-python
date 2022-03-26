fut = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional',
       'Cruzeiro', 'São Paulo',	'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia',
       'Goiás', 'Guarani', 'Sport', 'Portuguesa', 'Atlético Paranaense', 'Vitória')
print('Os 5 primeiros colocados são: ')
print(fut[0:5])

print('Os últimos 4 colocados são: ')
print(fut[-4:])

print('A ordem alfabética dos nomes são: ')
print(sorted(fut))

print(f'O time Botafogo está na posição: {fut.index("Botafogo") + 1}')



