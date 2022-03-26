# Leia a largura e a altura de uma parede em m, calcule sua area e a quantidade de tinta para pinta-la
# Cada 1litro de tinta pinta 2m2

altura = float(input('Qual a altura da sua parede? '))
largura = float(input('Qual a largura da sua parede? '))
area = altura * largura
quantidade = area / 2
print(f'A area da sua parede é {area}m², logo para pintar sua parede voce precisa de {quantidade} litros de tinta')
